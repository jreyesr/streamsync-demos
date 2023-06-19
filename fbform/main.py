import streamsync as ss

def handle_button_click(state):
    if state["name_not_exists"] or state["is_invalid_email"]:
        state.add_notification("error", "Can't submit", "Please correct the errors before submitting")
    else:
        state.add_notification("success", "Success!", "Your feedback was submitted successfully")
        print(state)

        # now reset the state
        state["name"] = ""
        onchange_name(state, "")
        state["email"] = ""
        onchange_email(state, "")
        state["further_contact"] = []
        state["feedback"] = ""


def onchange_name(state, payload):
    state["name_not_exists"] = not payload
    

def onchange_email(state, payload):
    state["show_further_contact"] = bool(payload)
    
    # Naive email validation, just for show
    # Empty email is considered valid, so the error msg does not appear
    import re
    state["is_invalid_email"] = payload and not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", payload)

initial_state = ss.init_state({
    "name": "",
    "email": "",
    "further_contact": [],
    "feedback": "",

    "show_further_contact": False,
    "is_invalid_email": False,
    "name_not_exists": True
})