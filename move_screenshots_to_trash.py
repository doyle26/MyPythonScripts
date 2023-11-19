import os
import shutil

# Set the source directory (your desktop folder)
desktop_path = os.path.expanduser("/Users/andrewdoyle/Desktop")

# Set the Trash directory
trash_path = os.path.expanduser("/Users/andrewdoyle/.Trash")

# Search for files containing "screenshot" in the desktop folder
files_to_move = []
for root, dirs, files in os.walk(desktop_path):
    for filename in files:
        if "screenshot" in filename.lower():
            files_to_move.append(os.path.join(root, filename))

# Print the current working directory
print("Current working directory:", os.getcwd())

# Print the list of files in the source directory before the move
print("Files in source directory before move:", os.listdir(desktop_path))

# Move the files to the Trash
for file_path in files_to_move:
    try:
        shutil.move(file_path, trash_path)
        print(f"Moved '{file_path}' to Trash")
    except Exception as e:
        error_message = f"Error moving '{file_path}' to Trash: {e}"
        print(error_message)
        with open('/Users/andrewdoyle/automate_shell_scripts/Error_Logs/error_log.txt', 'a') as log_file:
            log_file.write(error_message + '\n')

# Print the list of files in the source directory after the move
print("Files in source directory after move:", os.listdir(desktop_path))

print("Files moved to Trash.")


## Command in terminal after:
## crontab -e
## i (This is to edit it)
## 0 0 * * * /usr/bin/python3 Users/andrewdoyle/Documents/Python\ Scripts/move_screenshots_to_trash.py
## esc (when done)
## :wq (save and quite)
