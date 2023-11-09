import os
from dotenv import load_dotenv
#from twilio.rest import Client
load_dotenv()

def send_whatsapp_message(body):
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
    client = Client(account_sid, auth_token)

    # this is the Twilio sandbox testing number
    from_whatsapp_number='whatsapp:+14155238886'
    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number='whatsapp:+573014002491'

    message = client.messages.create(body=body,
                           from_=from_whatsapp_number,
                           to=to_whatsapp_number)
    print(message.sid)
#send_whatsapp_message('holaaaa')
