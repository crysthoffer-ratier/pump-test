import time
import json, csv

from datetime import datetime, timedelta
from pathlib import Path
from pump.carb import read_data_from_carb_pump
from pump.standard import read_data_from_standard_pump

from gpiozero import OutputDevice

# Initialize relay connected to GPIO pin 17
# relay1 = OutputDevice(17)

DEBUG_MODE = True


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
            with open(f, mode="w", newline="") as file:
                debug_message("Creating file...")

                csv_header = [
                    "pump",
                    "start_time",
                    "end_time",
                    "elapsed_time_ms",
                    "flowrate",
                    "volume",
                ]
                writer = csv.writer(file)
                writer.writerow(csv_header)  # Write the header

                debug_message("Done!")
            return True
        else:
            # If the file already exists, don't overwrite it
            debug_message(f"File '{f}' already exists.")
            return True
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


def csv_to_json(csv_file_path, json_file_path):
    # Read the CSV file
    with open(csv_file_path, mode="r") as csv_file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(csv_file)

        # Convert CSV to list of dictionaries
        rows = list(csv_reader)

    # Write the data to a JSON file
    with open(json_file_path, mode="w") as json_file:
        json.dump(rows, json_file, indent=4)


def append_to_file(file_path: str, data: str) -> None:
    """
    Appends a new row of data to a CSV file.

    Args:
        file_path (str): Path to the CSV file.
        data (list): A list of values to write as a new row in the CSV file.
    """
    try:
        with open(file_path, mode="a", newline="") as file:
            debug_message("Writing data...")
            writer = csv.writer(file)

            writer.writerow(data)
            print(f"Data: {data}")
    except Exception as e:
        debug_message(e)


def debug_message(msg: str) -> None:
    if DEBUG_MODE:
        print(f"[DEBUG]: {msg}")


def main() -> None:
    """
    Main function that runs the script, creates the CSV file (if not exists),
    and appends timestamped flowrate data to it.
    """
    csv_file_name = "data.csv"
    csv_file_path = Path(f"data/{csv_file_name}").resolve()
    json_file_name = "data.json"
    json_file_path = Path(f"data/{json_file_name}").resolve()

    start_time = time.time()

    if create_file(csv_file_path):

        while True:
            print("Checking...")
            elapsed_time = time.time() - start_time

            if elapsed_time >= 1:
                print("Collecting data...")

                carb_data = read_data_from_carb_pump()
                standard_data = read_data_from_standard_pump()
                print(carb_data)
                print(standard_data)
                append_to_file(csv_file_path, carb_data)

                time.sleep(0.1)  # Small delay to prevent CPU overload

            time.sleep(2)

            # csv_to_json(csv_file_path, json_file_path)

    # relay1.toggle()
    # time.sleep(3)


if __name__ == "__main__":
    print(__name__)
    main()
