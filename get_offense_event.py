import requests
import time
import os
from datetime import datetime
import config



def get_offense_event(offense_id):
    """
    Fetch the latest events associated with a given offense ID from QRadar.
    """
    # Fix: Use offense_id inside INOFFENSE() function
    QRADAR_OFFENSE_EVENTS_QUERY = f"""
    SELECT *
    FROM events 
    WHERE INOFFENSE({offense_id})
    LAST 7 DAYS
    """

    search_data = {"query_expression": QRADAR_OFFENSE_EVENTS_QUERY}

    print(f"Sending Query to QRadar: {QRADAR_OFFENSE_EVENTS_QUERY}")

    # Step 1: Start a search
    response = requests.post(config.QRADAR_API_URL, headers=config.HEADERS, params=search_data, verify=False)

    if response.status_code != 201:
        print(f"Error starting search for offense {offense_id}: {response.text}")
        return []

    search_id = response.json().get("search_id")
    print(f"Search started with ID: {search_id}")

    # Step 2: Poll for results
    search_status_url = f"{config.QRADAR_API_URL}/{search_id}"
    while True:
        time.sleep(2)  # Wait for 2 seconds before polling
        status_response = requests.get(search_status_url, headers=config.HEADERS, verify=False)
        status = status_response.json().get("status")

        print(f"Polling status: {status}")
        if status == "COMPLETED":
            break
        elif status == "ERROR":
            print(f"Error retrieving results: {status_response.text}")
            return []

    # Step 3: Retrieve search results
    results_url = f"{config.QRADAR_API_URL}/{search_id}/results"
    results_response = requests.get(results_url, headers=config.HEADERS, verify=False)

    if results_response.status_code != 200:
        print(f"Error retrieving results for offense {offense_id}: {results_response.text}")
        return []

    events = results_response.json().get("events", [])
    print(f"Retrieved {len(events)} events for Offense ID: {offense_id}")

    # Extract relevant fields
    formatted_events = [
        {
            "id": event.get("eventId"),
            "category": event.get("category"),
            "source_ip": event.get("sourceIp"),
            "destination_ip": event.get("destinationIp"),
            "timestamp": datetime.fromtimestamp(event.get("startTime") / 1000).strftime("%Y-%m-%d %H:%M:%S"),
        }
        for event in events
    ]

    return formatted_events

# Test Call
res = get_offense_event(12)
print(f" res = {res}")
