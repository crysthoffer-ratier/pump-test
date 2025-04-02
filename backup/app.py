import time
import json
import random
import csv

from datetime import datetime, timedelta
from pathlib import Path

from gpiozero import OutputDevice

# Initialize relay connected to GPIO pin 17
relay1 = OutputDevice(17)

def create_file(f: str) -> bool:
    """
    Creates a new file and writes a header to it.

    Args:
        f (str): The file path to create and write to.

    Returns:
        bool: Returns True if the file was created and header written successfully, 
              False if there was an error.
    """
    try:
        # Check if file already exists
        if not Path(f).exists():
            with open(f, mode='w', newline='') as file:
                csv_header = ["timestamp", "flowrate"]
                writer = csv.writer(file)
                writer.writerow(csv_header)  # Write the header
            return True
        else:
            # If the file already exists, don't overwrite it
            debug_message(f"File '{f}' already exists.")
            return False
    except Exception as e:
        debug_message(f"Error creating file: {e}")
        return False


def create_file1(f: str) -> bool:
    """
    Creates a new file if it doesn't exist.

    Args:
        f (str): The file path to create.

    Returns:
        bool: Returns True if the file was created, False if it already exists.
    """
    try:
        return open(f, "x")
    except Exception as e:
        debug_message(e)
        return False


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


def append_to_file(file_path: str, data: str) -> None:
    """
    Appends a new row of data to a CSV file.

    Args:
        file_path (str): Path to the CSV file.
        data (list): A list of values to write as a new row in the CSV file.
    """
    try:
        with open(file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(data)
    except Exception as e:
        debug_message(e)


def debug_message(msg: str) -> None:
    print(f"[DEBUG]: {msg}")


def main() -> None:
    """
    Main function that runs the script, creates the CSV file (if not exists),
    and appends timestamped flowrate data to it.
    """
    file_name = "data.csv"
    file_path = Path(f"data/{file_name}").resolve()


    create_file(file_path)
    
    # if not file_path.exists():
    #     create_file(file_path)
        # csv_header = ["timestamp", "flowrate"]
        # append_to_file(file_path, csv_header)

    data = [int(time.time()), round(random.uniform(1.91, 2.03), 2)]

    debug_message(data)

    append_to_file(file_path, data)

    # relay1.toggle()
    # time.sleep(3)


if __name__ == "__main__":
    main()
