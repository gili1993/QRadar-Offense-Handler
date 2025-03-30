import logging

LOG_FILE = "/Users/gililevy/Documents/QRadar Simpale Integration/qradar_offense_handler/offense_handler.log"

# Configure logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s -- %(message)s')

def log_message(message, level="info"):
    """
    Write log messages to file and print to console.
    """
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)

#log_message("test")