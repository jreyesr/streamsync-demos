import streamsync as ss
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

import datetime

# This is a placeholder to get you started or refresh your memory.
# Delete it or adapt it as necessary.
# Documentation is available at https://streamsync.cloud

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')



def _load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])#.map(datetime.datetime.isoformat)
    return data

    
# Initialise the state
data = _load_data(10000)

def data_for_hour(hr):
    import plotly.express as px

    filtered_data = data[data[DATE_COLUMN].dt.hour == hr]
    fig = px.density_mapbox(filtered_data, lat="lat", lon="lon",
                        zoom=8, height=300,
                        radius=10,
                        mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, autosize=True)
    return fig

def hex_for_hour(hr):
    import plotly.figure_factory as ff
    import plotly.express as px
    filtered_data = data[data[DATE_COLUMN].dt.hour == hr]

    fig = ff.create_hexbin_mapbox(
        filtered_data, lat="lat", lon="lon",
        nx_hexagon=10, opacity=0.9,
        min_count=1,
        show_original_data=True,
        original_data_marker=dict(size=4, opacity=0.6, color="deeppink"),
        mapbox_style="open-street-map",
    )
    fig.update_layout(margin=dict(b=0, t=0, l=0, r=0), width=100)
    return fig

def bars_for_hour(hr):
    import plotly.express as px

    new_data = data.copy()
    new_data[DATE_COLUMN] = new_data[DATE_COLUMN].map(lambda x: x.hour)

    color_discrete_sequence = ['#ec7c34']*24
    color_discrete_sequence[int(hr)] = '#609cd4'

    # fig = px.histogram(new_data, x=DATE_COLUMN,
    #     color=DATE_COLUMN,
    #     color_discrete_sequence=color_discrete_sequence)
    hist = pd.DataFrame(data={"x": np.arange(24), "count": np.histogram(new_data[DATE_COLUMN], bins=np.arange(25))[0]})
    
    fig = px.bar(hist, x="x", y="count",
        color=hist.x.map(str),
        color_discrete_sequence=color_discrete_sequence,
    )
    fig.update_layout(showlegend=False, autosize=True)
    return fig


def recalculate(state):
    state["plotly"] = data_for_hour(state["hod"])
    state["plotly_bars"] = bars_for_hour(state["hod"])

initial_state = ss.init_state({
    #"data": data,
    #"by_hour": hist_values,
    #"fig": fig,
    "hod": 17,
    "plotly": data_for_hour(17),
    "plotly_bars": bars_for_hour(17),
})

