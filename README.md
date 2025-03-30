# QRadar-Offense-Handler

# QRadar Offense Handler

A Python-based tool to fetch and analyze offenses from IBM QRadar using the QRadar API. The tool supports querying offenses, retrieving events related to specific offenses, and generating HTML reports.

## Features
- Fetch the latest offenses from QRadar.
- Retrieve event data for specific offenses.
- Generate detailed HTML reports for analysis.
- Log activities and errors for troubleshooting.

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

