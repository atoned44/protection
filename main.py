import os
import requests
from datetime import datetime
from pytz import timezone
import logging

# Set the Pushsafer API URL and access key
PUSHSAFER_URL = "https://www.pushsafer.com/api"
pushsafer_access_key = os.environ.get("PUSHSAFER_ACCESS_KEY")

# Set the timezone for London
LONDON_TZ = timezone("Europe/London")

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_notification():
    # Get the current time in the London timezone
    now = datetime.now(LONDON_TZ)
    hour = now.hour

    # Set the URL of your static webpage with the message
    message_url = "https://atoned44.github.io/protection/"
    
    # Set the notification payload with the link to the message and other parameters
    payload = {
        "k": pushsafer_access_key,
        "m": f"Recite your incantations, spells & mantras @ {message_url}",
        "u": message_url,
        "s": "1",
    }

    # Send the notification via the Pushsafer API
    try:
        response = requests.post(PUSHSAFER_URL, data=payload)
        if response.status_code == 200:
            logging.info("Notification sent successfully.")
        else:
            logging.error(f"Failed to send notification: {response.text}")
    except requests.exceptions.Timeout as e:
        logging.error(f"Failed to send notification due to timeout: {e}. Retrying in 5 minutes.")
        time.sleep(300)

# run the function
send_notification()
