import time
import subprocess

# Replace these with your actual contact information and message
recipient_name = "14156291817"
message = "Hello, this is your automated message!"
send_time = "21:00"  # Replace with the desired time in HH:MM format

# Function to send the message
def send_message():
    applescript_code = f'''
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set theBuddy to buddy "{recipient_name}" of targetService
        send "{message}" to theBuddy
    end tell
    '''
    subprocess.run(['osascript', '-e', applescript_code])

# Get the current time
current_time = time.strftime("%H:%M")

# Check if the current time is equal to the specified send_time
if current_time == send_time:
    send_message()
else:
    print(f"Message will be sent at {send_time}.")

# You can manually run this script at the specified send_time, and it will send the message if the times match.
