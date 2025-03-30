from log_message import log_message
from get_offense_event import get_offense_event

from jinja2 import Environment, FileSystemLoader
import json
import os
from datetime import datetime


# Define Parameters
TEMPLATE_DIR = "/Users/gililevy/Documents/QRadar Simpale Integration/qradar_offense_handler/templates"

def datetimeformat(value):
    """
    Convert timestamp to readable date-time format.
    """
    try:
        formatted_time = datetime.fromtimestamp(int(value) / 1000).strftime("%Y-%m-%d %H:%M:%S")
        log_message(f"Formatted timestamp {value} -> {formatted_time}")
        return formatted_time
    except Exception as e:
        log_message(f"Error formatting timestamp {value}: {e}")
        return "Invalid Date"

# Initialize Jinja Environment and Register the Filter
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
env.filters['datetimeformat'] = datetimeformat  # Register filter before loading template
log_message("Registered 'datetimeformat' filter in Jinja2")

# Template Mapping
templates = {
    "Malware": "malware_template.html",
    "Phishing": "phishing_template.html",
    "Unauthorized Access": "access_template.html",
    "Default": "generic_template.html"
}
log_message("Template mapping initialized")

def select_template(offense):
    """
    Select the appropriate HTML template based on offense category.
    """
    offense_id = offense.get('id', 'Unknown')
    log_message(f"Selecting template for Offense ID: {offense_id}")

    category = offense.get("category", "Default")
    selected_template = templates.get(category, templates["Default"])
    
    log_message(f"Selected template for Offense ID {offense_id}: {selected_template}")
    return selected_template

def html_report(offense):
    """
    Generate an HTML report for the given offense.
    """
    #print(offense)
    offense_id = offense.get('id', 'Unknown')
    log_message(f"Generating HTML report for Offense ID: {offense_id}")

    # Load the template
    template_name = select_template(offense)
    try:
        template = env.get_template(template_name)  # Now loading the template correctly
        log_message(f"Successfully loaded template: {template_name}")
    except Exception as e:
        log_message(f"Error loading template '{template_name}': {e}")
        return None

    # Get offense events
    offense_event = get_offense_event(offense_id=offense)
    print(offense_event)

    # Create a report dictionary
    report = {
        "generated_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "offenses": [offense],
    }
    log_message(f"Report dictionary created for Offense ID: {offense_id}")

    # Generate and save the report
    output_path = f"/Users/gililevy/Documents/QRadar Simpale Integration/qradar_offense_handler/reports/offense{offense_id}.html"
    
    try:
        rendered_html = template.render(report=report)
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(rendered_html)
        log_message(f"Report successfully saved at: {output_path}")
        return {"file_path": output_path, "html_content": rendered_html}
    except Exception as e:
        log_message(f"Error saving report for Offense ID {offense_id}: {e}")
        return None
