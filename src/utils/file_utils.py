import json, csv
from utils.debug_utils import debug_message

from pathlib import Path

csv_file = "data.csv"
json_file = "data.json"
path = Path(f"data").resolve()


def run_file_checks() -> bool:
    debug_message("Running file checks...")

    file_path = path/csv_file

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


def append_to_file(file_path: Path, data: list) -> None:
    try:
        with open(file_path, mode='a', newline='') as file:
            debug_message(f"Writing data in {file_path}")

            writer = csv.writer(file)
            writer.writerow(data)

            debug_message(f"Done.")
    except (OSError, IOError) as e:
        debug_message(f"File operation error: {e}")
    except Exception as e:
        debug_message(e)