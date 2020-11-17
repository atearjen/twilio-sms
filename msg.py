# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

import schedule, random, time 

GOOD_MORNING_QUOTES =[
    "Good Morning Pal!",
    "I hope you have the best day ever!"
]

def send_message(quotes_list = GOOD_MORNING_QUOTES):
    # you will need the account number and token from twilio to authenticate our client 
    account = os.environ['TWILIO_ACCOUNT_SID']
    token = os.environ['TWILIO_AUTH_TOKEN']
    twilio_number = os.environ['TWILIO_NUMBER']
    cellphone = os.environ['TRIAL_NUMBER']
    client = Client(account,token)
    quote = quotes_list[random.randint(0,len(quotes_list)-1)]
    client.messages \
                .create(
                     body=quote,
                     from_=twilio_number,
                     to=cellphone
                 )

send_message()
# If you want to schedule does current time zone that I am in 
# schedule.every().day.at("14:37").do(send_message,GOOD_MORNING_QUOTES)

# while True:
#     # checkes whether a schedule task
#     # is pending to run or not 
#     schedule.run_pending()
#     time.sleep(2)