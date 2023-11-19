import subprocess
import datetime
import time

# Replace '1234567890' with the phone number you want to send the message to
phone_number = '14156291817'

# Replace 'Your message here' with the message you want to send
message = 'test'

# Set the date and time to send the message (24-hour format)
send_time = datetime.datetime(year=2023, month=11, day=7, hour=20, minute=59, second=0)

# Calculate the time delay until the specified time is reached
current_time = datetime.datetime.now()
time_difference = send_time - current_time
time_delay = time_difference.total_seconds()

if time_delay > 0:
    print(f"Waiting for {time_delay} seconds until the specified time...")
    time.sleep(time_delay)

applescript = f"""
tell application "Messages"
    set targetService to 1st service whose service type = iMessage
    set targetBuddy to buddy "+1{phone_number}" of targetService
    send "{message}" to targetBuddy
end tell
"""

subprocess.call(['osascript', '-e', applescript])
