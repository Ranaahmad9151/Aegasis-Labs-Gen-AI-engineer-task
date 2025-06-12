from utils.hubspot_api import create_contact, update_contact, create_deal

def hubspot_agent(action, payload):
    if action == "create_contact":
        return create_contact(payload)
    elif action == "update_contact":
        return update_contact(payload)
    elif action == "create_deal":
        return create_deal(payload)
    else:
        return {"error": f"Unsupported action: {action}"}
