import time
import json

# Spotify
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Mail Notification (didnt code yet)
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMS Notification
from twilio.rest import Client

# Discord Notification (didnt code yet)
#import discord
#from discord.ext import commands


with open('secret_keys.json') as f:
    secrets_json = f.read()
    
secrets = json.loads(secrets_json)
print(secrets['account_sid'])


# Twilio configuration
account_sid = secrets['account_sid']
auth_token = secrets['auth_token']
twilio_phone_number = secrets['twilio_phone_number']
receiver_phone_number = secrets['receiver_phone_number']


def send_sms(message:str) -> None:
    client = Client(account_sid, auth_token)
    client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=receiver_phone_number
    )


# Set up Spotify authentication
scope = secrets['scope']
client_id = secrets['client_id']
client_secret = secrets['client_secret']
redirect_uri = secrets['redirect_uri']


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, 
                                               client_id=client_id, 
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri))


# Retrieve the initial current user's total followers count
user_profile = sp.current_user()
follower_count = user_profile['followers']['total']
print(f"Initial Followers Count: {follower_count}")


while True:
    # Retrieve the updated current user's profile information in each iteration
    profile = sp.current_user()
    temp_follower_count = user_profile['followers']['total']

    if temp_follower_count < follower_count:
        message = f'{follower_count - temp_follower_count} people unfollowed you! 😧\nCurrent Followers Count: {temp_follower_count}'
        send_sms(message)
        print(message)
        follower_count = temp_follower_count

    elif temp_follower_count > follower_count:
        message = f'{temp_follower_count - follower_count} people followed you! 🤩\nCurrent Followers Count: {temp_follower_count}'
        send_sms(message)
        print(message)
        follower_count = temp_follower_count

    else:
        pass

    time.sleep(3)
