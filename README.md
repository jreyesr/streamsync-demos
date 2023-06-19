# Streamsync examples

This repo contains a set of sample apps for the [Streamsync](https://www.streamsync.cloud/) framework, intended to explore the framework and how well it fares in a few scenarios, some of which are not its intended functionality (data apps, like [Streamlit](https://streamlit.io/))

This repo is a companion to [this blog post]()

## Running

To run an app:

1. Install Streamsync with `pip install streamsync`
1. Clone this repo and `cd` into it
1. Run the desired example with `streamsync edit <folder_name>`

For more instructions, refer to [Streamsync's docs](https://www.streamsync.cloud/getting-started.html)

## Apps

### uber

A reimplementation of [Streamlit's starter tutorial](https://docs.streamlit.io/library/get-started/create-an-app), a data app that displays some data about an Uber ride dataset

### fbform

A sample feedback form that asks a user for a name, email, and comments. Intended to test the usefulness of Streamsync to create dynamic web forms, with conditional fields and validation

### usermgmt

A reimplementation of [Retool's starter tutorial](https://docs.retool.com/docs/retool-fundamentals), intended to test the ability of Streamsync to emulate a fully-fledged low-code "internal apps" builder.
