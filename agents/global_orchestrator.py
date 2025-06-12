from openai import OpenAI
from utils.config_loader import load_config
from agents.hubspot_agent import hubspot_agent
from agents.email_agent import email_agent

config = load_config()
client = OpenAI(api_key=config["openai_api_key"])

def global_orchestrator(user_query):
    # Use LLM to interpret query & decide action
    # (for real use LangChain or OpenAI tools for structured function calling)
    
    if "create contact" in user_query.lower():
        payload = {
            "properties": {
                "email": "new@example.com",
                "firstname": "John",
                "lastname": "Doe"
            }
        }
        result = hubspot_agent("create_contact", payload)
        email_agent("Contact Created", "New contact was added successfully.", "you@example.com")
        return result

    return {"error": "Could not determine action"}
