import time
from datetime import datetime, timedelta
from pathlib import Path
from pump.carb import read_data_from_carb_pump
from pump.standard import read_data_from_standard_pump

from gpiozero import OutputDevice

import utils.file_utils as file_utils

# Initialize relay connected to GPIO pin 17
# relay1 = OutputDevice(17)


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
    previous_date = current_date - timedelta(days=1)

    return current_date.strftime("%Y-%m-%d"), previous_date.date().strftime("%Y-%m-%d")


def main():
    if file_utils.run_file_checks():
        while True:
            pump1 = read_data_from_carb_pump()
            pump2 = read_data_from_standard_pump()

            file_utils.append_to_file(pump1)
            file_utils.append_to_file(pump2)

            time.sleep(5)

if __name__ == "__main__":
    main()
