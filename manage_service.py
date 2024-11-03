#assuming code runs from  home/cron_jobs as (manage_service.py)
import os
import subprocess
import shutil
import tempfile

    
# a service is a program that runs in the background to restart a service and clear temp folder

# command to get service name

# systemctl list-units --type=service

# writing command programmatically
def list_services():
    try:
        # Execute the command and capture the output
        result = subprocess.run(['systemctl', 'list-units', '--type=service'])

        # Print the output of the command
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.stderr}")




# Function to restart a service
def restart_service(service_name):
    try:
        subprocess.run(['sudo', 'systemctl', 'restart', service_name], check=True)
        print(f"Service '{service_name}' restarted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error restarting service '{service_name}': {e}")

# Function to clear the temp folder
def clear_temp_folder(temp_folder):
    try:
        if os.path.exists(temp_folder):
            shutil.rmtree(temp_folder)  # Remove existing temp folder
        os.makedirs(temp_folder)  # Recreate temp folder
        print(f"Temporary folder '{temp_folder}' cleared successfully.")
    except Exception as e:
        print(f"Error clearing temporary folder '{temp_folder}': {e}")

if __name__ == "__main__":
    SERVICE_NAME = "bluetooth.service"  # Replace with your service name
    # TEMP_FOLDER = tempfile.gettempdir()  # Use default system temp folder(NOT WORKING, PERMISSION ERROR)
    TEMP_FOLDER ='my_temp_folder'  # Use a  different temp folder
    
    # Restart the service and clear temp folder
    restart_service(SERVICE_NAME)
    clear_temp_folder(TEMP_FOLDER)


# get list of services
# list_services()

# example of a service name
# "my_service_name.service"

# scheduling it with crontab
# $crontab -e( to edit the cronfile) and add the line below to run the script every day at 2am
# 0 2 * * * /usr/bin/python3 /home/ali/cron_jobs/manage_service.py >> /Users/your_username/cron_jobs/cron_log.txt 2>&1
# $crontab -l( to list the scheduled jobs) 

