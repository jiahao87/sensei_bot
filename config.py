"""Config file

Please input your configurations here
"""

# Telegram bot token
BOT_TOKEN = None

# Path to Google service account Json file , e.g., 'My First Project-XXX.json'
# See more details at: https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys
GOOGLE_APPLICATION_CREDENTIALS = None

# Google Storage bucket name
BUCKET_NAME = None

# Telegram user ID, steps to get ID see: https://www.wikihow.com/Know-Chat-ID-on-Telegram-on-Android
# Putting a telegram ID will allow only the specified ID to talk to bot
TELEGRAM_ID = None

# See supported language code and texttospeech name here:
# https://cloud.google.com/text-to-speech/docs/voices
LANGUAGE_CODE = "ja-JP"
TEXTTOSPEECH_NAME = "ja-JP-Wavenet-A"

# Options for the Telegram menu buttons 
menu_options = {'1': {  
                        'option':"1) How to pronounce JP word(s)",
                        'reply': "Ok, let's hear the pronunciation of JP word(s). \n\nEnter the JP word(s) into the chat box"
                },
                '2': {
                        'option':"2) How to say (EN) in JP",
                        'reply': "Ok, let's learn how to say (EN) in JP. \n\nWhat is/are the EN word(s)?"
                }
}
