
# Manage Service and Clear Temporary Folder

This project contains a Python script (`manage_service.py`) designed to automate two tasks:

1. Restart a specified system service.
2. Clear a specified temporary folder.

## Prerequisites

- **OS**: Unix-based systemsf (Linux)
- **Python**: Python 3 must be installed.
- **Permissions**: Requires root or sudo privileges to restart services.

### Dependencies

The script uses Python's built-in libraries:
## Modules Used

### 1. `os`
The `os` module provides a way of using operating system-dependent functionality, such as interacting with file systems, executing system commands, and managing directories.

**Usage in this script:**
- `os.path.exists(temp_folder)`: Checks if the specified directory exists.
- `os.makedirs(temp_folder)`: Creates the specified directory.
  
### 2. `subprocess`
The `subprocess` module lets you run other programs from within your Python script. It also lets you send input to these programs, receive their output, handle any errors, and check if they ran successfully.

**Usage in this script:**
- `subprocess.run(['systemctl', 'list-units', '--type=service'])`: Lists all active system services on Unix-based systems.
- `subprocess.run(['sudo', 'systemctl', 'restart', service_name], check=True)`: Restarts the specified system service (requires `sudo` privileges).

### 3. `shutil`
The `shutil` module offers a high-level interface for file operations, such as copying and removing files and directories.

**Usage in this script:**
- `shutil.rmtree(temp_folder)`: Removes the specified temporary folder and all its contents.

### 4. `tempfile`
The `tempfile` module generates temporary files and directories, ensuring they are unique to prevent conflicts.

**Usage in this script:**
- `tempfile.gettempdir()`: Retrieves the default temporary directory path for the system.


## Setup Instructions

### Step 1: Create the Directory

If not already created, set up a directory for cron jobs:
```bash
mkdir ~/cron_jobs
cd ~/cron_jobs
```

### Step 2: Create or Download `manage_service.py`

Place the `manage_service.py` script in the `~/cron_jobs` directory.

### Step 3: Update Script Variables

Open `manage_service.py` and modify the following variables:

- **SERVICE_NAME**: Specify the name of the service to restart. 
  - Example: `bluetooth.service` for Linux.
- **TEMP_FOLDER**: Specify the path to the temporary folder you want to clear. 
  - By default, this is set to use the system's default temp directory. If permissions restrict access, you may set a custom folder like `'my_temp_folder'`.

Example:
```python
SERVICE_NAME = "bluetooth.service"  # Update with your target service name
TEMP_FOLDER = '/path/to/temp/folder'  # Update with your target temp folder path
```

## Usage Instructions

To run the script manually:
```bash
python3 manage_service.py
```

### Script Functionality

- **Restart a Service**: The script will attempt to restart the specified service using `systemctl`.
- **Clear Temporary Folder**: The script will delete and recreate the specified temporary folder, effectively clearing all its contents.

### Cron Job Setup

1. **Open crontab editor**:
   ```bash
   crontab -e
   ```

2. **Add a cron job entry** to execute the script at a specified time. For example, to run the script every day at 2 AM:
   ```bash
   0 2 * * * /usr/bin/python3 /home/your_username/cron_jobs/manage_service.py >> /home/your_username/cron_jobs/cron_log.txt 2>&1
   ```

3. **Save and exit** the editor.

4. **Verify the cron job**:
   ```bash
   crontab -l
   ```

The cron job will run daily at 2 AM, restarting the specified service and clearing the temp folder. Output and errors will be logged in `cron_log.txt`.

### Example Commands in the Script

- **Restarting a Service**:
  ```python
  restart_service(SERVICE_NAME)
  ```
- **Clearing the Temp Folder**:
  ```python
  clear_temp_folder(TEMP_FOLDER)
  ```

## Troubleshooting

- **Permission Denied**: If you encounter permissions errors with the temp folder, ensure that the script points to a directory with accessible permissions.
- **Service Not Found**: Ensure the service name is correct by listing services with:
  ```bash
  systemctl list-units --type=service
  ```

## Additional Notes


- **Logging**: `>> /home/your_username/cron_jobs/cron_log.txt 2>&1` appends output and error logs for easier debugging.

## License

This script is provided "as-is" without any warranties or guarantees. Please test carefully in your environment.
