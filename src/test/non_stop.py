import time
import random
import logging

import sys
import os

# Add the src directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Now you can import from the utils directory
from utils.file_utils import append_to_file
from utils.debug_utils import debug_message

def non_stop_test():
    try:
        start_time = time.time()

        flow_rate = random.uniform(1.52, 2.147)
        total_volume = random.uniform(0.12, 0.16)

        end_time = time.time()

        elapsed_time_ms = (
            end_time - start_time
        ) * 1000  # Convert seconds to milliseconds

        debug_message(
            [
                "CARBONATION",
                start_time,
                end_time,
                f"{elapsed_time_ms:.4f}",
                flow_rate,
                total_volume,
            ],
            logging.INFO,
        )
        
        append_to_file(
            [
                "CARBONATION",
                start_time,
                end_time,
                f"{elapsed_time_ms:.4f}",
                flow_rate,
                total_volume,
            ]
        )
        time.sleep(5)
    except Exception as e:
        debug_message(f"{e}", logging.ERROR)


while True:
    non_stop_test()
