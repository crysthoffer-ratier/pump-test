import datetime
import json
import logging
import utils.debug_utils as debug_utils

from pathlib import Path

path = Path(f"src").resolve()


def read_config_file() -> dict:     
    script_dir = Path(__file__).resolve().parent.parent
    file_path = script_dir / 'config.json'

    #debug_utils.debug_message(f"Looking for config file at: {file_path}", logging.INFO)

    try:
        with open(file_path) as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file '{file_path}' not found.")
    except json.JSONDecodeError:
        raise ValueError(f"Error decoding JSON in the configuration file '{file_path}'.")


def get_dates() -> datetime:
    """
    Returns the current date and the previous date in YYYY-MM-DD format.

    The function calculates the current date using the current system time and
    computes the previous date by subtracting one day from the current date.
    Both dates are returned as strings formatted as 'YYYY-MM-DD'.

    Returns:
        tuple: A tuple containing two strings:
            - The current date (today's date) in 'YYYY-MM-DD' format.
            - The previous date (yesterday's date) in 'YYYY-MM-DD' format.
    """
    current_date = datetime.now()
    previous_date = current_date - datetime.timedelta(days=1)

    return current_date.strftime("%Y-%m-%d"), previous_date.date().strftime("%Y-%m-%d")

