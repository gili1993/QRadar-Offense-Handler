# QRadar Offense Handler

A Python-based tool to fetch and analyze offenses from IBM QRadar using the QRadar API. The tool supports querying offenses, retrieving events related to specific offenses, and generating HTML reports.

## Features
- Fetch the latest offenses from QRadar.
- Retrieve event data for specific offenses.
- Generate detailed HTML reports for analysis.
- Log activities and errors for troubleshooting.
- Supports efficient polling for event data with configurable intervals.
- Generates user-friendly HTML reports with offense details and event information.
- Uses robust error handling and logging to ensure consistent performance.

## Project Structure and Workflow
The project is organized into modular Python scripts and configuration files to ensure clarity and separation of concerns.

### Components:
- **config.py:** Contains API configurations, including the QRadar API URL and token.
- **fetch_new_offense.py:**
  - Fetches the latest offense from QRadar.
  - Uses the API URL and token from the `config.py` file.
  - Logs the process and saves the offense ID to track the last processed offense.
- **get_offense_event.py:**
  - Retrieves events related to a specific offense ID from QRadar.
  - Uses a polling mechanism to wait for search results.
  - Extracts important event details like source IP, destination IP, category, and timestamp.
- **html_report.py:**
  - Generates HTML reports summarizing offense and event data.
  - Uses templates from the `templates/` directory.
- **log_message.py:**
  - A utility script to handle structured logging.
  - Creates and maintains the `offense_handler.log` file.
- **main.py:**
  - The primary entry point to initiate the offense fetching and reporting process.
- **templates/:**
  - Contains HTML templates used to generate formatted reports.
- **logs/:**
  - Stores log files with details of successful operations and errors.

### Workflow:
1. **Initialization:**
   - The `config.py` file sets up the API URL and token.
2. **Fetching Offense:**
   - The script `fetch_new_offense.py` retrieves the latest offense from QRadar.
   - Logs the process and saves the last processed ID.
3. **Fetching Event Data:**
   - `get_offense_event.py` retrieves the events related to the fetched offense.
   - Uses polling to wait for results if the data is not immediately available.
4. **Generating Report:**
   - The `html_report.py` script creates an HTML file summarizing the offense and related events.
5. **Logging:**
   - All operations and errors are logged in `offense_handler.log`.
  ![Uploading image.png…]()


## Prerequisites
- Python 3.8 or higher
- QRadar API access and token
- Internet access to connect to the QRadar server

## Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/qradar-offense-handler.git
cd qradar-offense-handler
```

Install the required packages:
```bash
pip install -r requirements.txt
```

## Configuration
The API token and URL are defined in the `config.py` file.

Example `config.py`:
```python
# QRadar API Configuration
QRADAR_API_URL = "https://10.100.102.111/api/ariel/searches"
QRADAR_API_TOKEN = "ccc8f580-c6cc-42bc-ad61-b5bb58b5ffaf"

HEADERS = {
    "Content-Type": "application/json",
    "SEC": QRADAR_API_TOKEN,
    "Version": "12.0"
}
```

> **Warning:** Avoid committing your API token to public repositories.

## Usage
To fetch new offenses:
```bash
python fetch_new_offense.py
```

To retrieve events for a specific offense:
```bash
python get_offense_event.py
```

## Logging
Logs are stored in the `offense_handler.log` file, capturing both successful operations and errors.

## HTML Report Generation
HTML reports are saved in the `reports` folder and can be viewed in any web browser.

## Contributing
Contributions are welcome! Please submit a pull request with your proposed changes.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

