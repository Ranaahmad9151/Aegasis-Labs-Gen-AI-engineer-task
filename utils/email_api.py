import sendgrid
from sendgrid.helpers.mail import Mail
from utils.config_loader import load_config

config = load_config()

def send_email(subject, content, to_email):
    sg = sendgrid.SendGridAPIClient(config["sendgrid_api_key"])
    email = Mail(from_email=config["sender_email"], to_emails=to_email,
                 subject=subject, plain_text_content=content)
    return sg.send(email)
