from utils.email_api import send_email

def email_agent(subject, message, to_email):
    return send_email(subject, message, to_email)
