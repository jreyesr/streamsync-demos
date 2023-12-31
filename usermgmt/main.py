import os
from typing import Any

import streamsync as ss
from dotenv import load_dotenv
import httpx # This is sometimes pulled in by FastAPI

load_dotenv()  # now the contents of .env are available on os.environ/os.getenv
client = httpx.Client(base_url=os.environ["API_URL"]) # Could also add auth details here, if they existed!

def action_clicked(state, payload, context, *args, **kwargs):
    current_user = context["item"]
    print(current_user)
    print("Toggling user", current_user["id"])
    # Call the REST API
    
    get_all_users() # Refresh the users, if the REST API worked...

def get_all_users() -> list[dict[str, Any]]:
    """Fetches all users from the remote API"""
    return client.get("/").json()


def prepare_users(users: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {str(u["id"]): u | {"unblocked": not u["blocked"], "action": "Unblock" if u["blocked"] else "Block"} for u in users}


# Initial state
ss.init_state({
    "users": prepare_users(get_all_users())
})