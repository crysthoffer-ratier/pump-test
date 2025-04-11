import time
import logging

from utils import misc, debug_utils
from test.non_stop import non_stop_test


def main():
    while True:        
        debug_utils.debug_message(f"Running Non Stop Test!", logging.DEBUG)
        non_stop_test()
        
        time.sleep(misc.read_config_file()["TEST"]["PUMP_OFF_TIME"])


if __name__ == "__main__":
    debug_utils.debug_message(f"Running test!", logging.INFO)
    main()
