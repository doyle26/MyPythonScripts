import subprocess

# Replace 'Contact Name' with the actual name of the contact in your Messages app
contact_name = '‭14156291817‬'

# Replace 'Your message here' with the message you want to send
message = 'Hello Bobo!!!'

applescript = f"""
tell application "Messages"
    set targetService to 1st service whose service type = iMessage
    set targetBuddy to buddy "{contact_name}" of targetService
    send "{message}" to targetBuddy
end tell
"""

subprocess.call(['osascript', '-e', applescript])
