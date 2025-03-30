from log_message import log_message 
import os
import requests
import config
# Ignore warnnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

log_message("QRadar API configuration set.")

# File to store last processed offense ID
LAST_OFFENSE_FILE = "/Users/gililevy/Documents/QRadar Simpale Integration/qradar_offense_handler/last_offense_id.txt"

def fetch_new_offense():
    """
    Fetch new offenses from QRadar API and return the new one.
    """
    log_message("Fetching new offense from QRadar API.")
    last_offense_id = get_last_offense_id()

    try:
        response = requests.get(f"{config.QRADAR_API_URL}/{last_offense_id}", headers=config.HEADERS, timeout=10, verify=False)
        
        response.raise_for_status()  # Call separately
        log_message("QRadar API request successful.")  

    except requests.exceptions.RequestException as e:
        log_message(f"Error fetching offenses: {e}", level="error")
        return None  # Return None instead of leaving it empty

    new_offense = response.json()
    return new_offense

def get_last_offense_id():
    """
    Retrieve the last processed offense ID from a file.
    """
    log_message("Fetching last processed offense ID.")
    if os.path.exists(LAST_OFFENSE_FILE):
        with open(LAST_OFFENSE_FILE, "r") as f:  # Open in read mode
            try:
                last_id = int(f.read().strip())  # Convert to int safely
                log_message(f"Last processed offense ID: {last_id}")
                #last_id + 1  # Add 1 for the next offense
                return last_id 
            except ValueError:
                log_message("Invalid last offense ID found, resetting to 0.", level="warning")
                return 0  # Handle invalid file content

    log_message("No last offense ID found, returning 0.")
    return 0  # Default return
