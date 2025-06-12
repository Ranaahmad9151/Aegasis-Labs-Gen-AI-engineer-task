from hubspot import HubSpot
from utils.config_loader import load_config

config = load_config()
client = HubSpot(api_key=config["hubspot_api_key"])

def create_contact(data):
    return client.crm.contacts.basic_api.create(data)

def update_contact(data):
    contact_id = data.pop("id")
    return client.crm.contacts.basic_api.update(contact_id, data)

def create_deal(data):
    return client.crm.deals.basic_api.create(data)
