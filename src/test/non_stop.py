import time
import random
import logging
from utils import debug_utils, misc


def non_stop_test():
    try:
        start_time = time.time()

        flow_rate = random.uniform(1.52, 2.147)
        total_volume = random.uniform(0.12, 0.16)

        end_time = time.time()

        elapsed_time_ms = (
            end_time - start_time
        ) * 1000  # Convert seconds to milliseconds

        debug_utils.debug_message(
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
    except Exception as e:
        debug_utils.debug_message(f"{e}", logging.ERROR)
