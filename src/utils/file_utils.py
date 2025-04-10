import json, csv
from utils.debug_utils import debug_message

from pathlib import Path

csv_file = "data.csv"
json_file = "data.json"
path = Path(f"data").resolve()


def run_file_checks() -> bool:
    debug_message("Running file checks...")

    script_dir = Path(__file__).resolve().parent.parent.parent  # This will give the directory inside src
    file_path = script_dir / "data" / csv_file

    if not _check_file(file_path):
        return _create_file(file_path)

    return True


def _check_file(file_path: Path) -> bool:
    if file_path.exists():
        debug_message(f"File '{file_path}' already exists.")
        return True

    debug_message(f"File '{file_path}' does not exist.")
    return False


def _create_file(file_path: Path) -> bool:
    try:
        with open(file_path, mode="w", newline="") as file:
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
    except Exception as e:
        debug_message(f"Error creating file: {e}")
        return False


def csv_to_json(file_path: Path) -> bool:
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            rows = list(csv_reader)

        json_file_path = path / json_file
        with open(json_file_path, mode="w", encoding="utf-8") as file:
            json.dump(rows, file, indent=4)

        debug_message(f"CSV data successfully converted to JSON at {json_file_path}.")
        return True
    except FileNotFoundError:
        debug_message(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError as e:
        debug_message(f"Error: Failed to decode JSON data. {e}")
    except csv.Error as e:
        debug_message(f"Error: Failed to read CSV file. {e}")
    except Exception as e:
        debug_message(f"Unexpected error: {e}")

    return False


def append_to_file(data: list) -> None:
    file_path = path / csv_file

    try:
        with open(file_path, mode="a", newline="") as file:
            debug_message(f"Appending data to {file_path}...")

            writer = csv.writer(file)
            writer.writerow(data)

            debug_message("Data appended successfully.")
    except (OSError, IOError) as e:
        debug_message(f"File operation error: {e}")
    except Exception as e:
        debug_message(e)
