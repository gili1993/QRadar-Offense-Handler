from log_message import log_message
from fetch_new_offense import fetch_new_offense
from html_report import html_report

def main():
        """
        Main function to fetch, process, and save new offenses.
        """
        log_message("Starting offense process.")
        new_offense = fetch_new_offense() # Retrieve new offense.
        print(f"new_offense = {new_offense}")
        html_report(new_offense)
        #print(new_offense)


if __name__ == "__main__":
    log_message("Starting script execution.")
    main()
    log_message("Processing completed.")
