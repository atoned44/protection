import os
import requests
import schedule
import time
from datetime import datetime
from pytz import timezone

# Set the Pushsafer API URL and access key
PUSHSAFER_URL = "https://www.pushsafer.com/api"
pushsafer_access_key = os.environ.get("PUSHSAFER_ACCESS_KEY")

# Set the timezone for London
LONDON_TZ = timezone("Europe/London")

def send_notification():
    # Get the current time in the London timezone
    now = datetime.now(LONDON_TZ)
    hour = now.hour

# Set the URL of your static webpage with the message
        message_url = "https://atoned44.github.io/protection/"
        
        # Set the notification payload with the link to the message and other parameters
        payload = {
            "k": pushsafer_access_key,
            "m": f"Recite this spell at {message_url}",
            "u": message_url,
            "s": "1",
        }

        # Send the notification via the Pushsafer API
        try:
            response = requests.post(PUSHSAFER_URL, data=payload)
            if response.status_code == 200:
                print("Notification sent successfully.")
            else:
                print(f"Failed to send notification: {response.text}")
        except Exception as e:
            print(f"Failed to send notification: {e}")

# Schedule the send_notification function to run every 2 hours
schedule.every(2).hours.do(send_notification)

# Run the scheduled tasks indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)
