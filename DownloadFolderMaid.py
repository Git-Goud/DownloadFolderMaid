import os
import time

#Download Folder Location
download_folder = "C:/Users/Kristen/Downloads/"

# Get the current time
current_time = time.time()

# Define the age limit (in seconds)
age_limit = 7 * 24 * 60 * 60 # One week

# Loop through all the files in the download folder
for filename in os.listdir(download_folder):
    file_path = os.path.join(download_folder, filename)

    # Check if the file is older than the age limit
    if os.path.isfile(file_path) and current_time - os.path.getctime(file_path) > age_limit:
        os.remove(file_path) # Delete the file

        # Print a message to confirm the file has been deleted
        print("Deleted file:", file_path)
