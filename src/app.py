import time
import logging

from utils import misc, file_utils as file_utils, debug_utils as debug_utils

from gpiozero import OutputDevice
from pump.carb import read_data_from_carb_pump

from test.non_stop import non_stop_test

relay_pin = 27
relayCarbPump = OutputDevice(relay_pin)


def test():
    debug_utils.debug_message(f"Running test!", logging.INFO)
    non_stop_test()

def main():
    config = misc.read_config_file()
    
    if file_utils.run_file_checks():
        try:
            while True:                            
                # Turn on pump
                relayCarbPump.on()
                debug_utils.debug_message(f"Carb pump ON for {config['PUMP_ON_TIME']} seconds", logging.INFO)
                test1.test_no_stop()

                time.sleep(config["PUMP_ON_TIME"])
                
                # Turn off pump
                relayCarbPump.off()
                debug_utils.debug_message(f"Carb pump ON for {config['PUMP_OFF_TIME']} seconds", logging.INFO)
                time.sleep(config["PUMP_OFF_TIME"])
                
                # TODO: Add support for standard pump data logging
        except Exception as e:
            logging.error(f"Error: {e}", exc_info=True)
        except KeyboardInterrupt:
            print("Interrupted by user. Shutting down.")
        finally:
            relayCarbPump.off()  # Ensure pump is off


if __name__ == "__main__":
    # main()
    test()
