import time
import logging
import json

import utils.file_utils as file_utils
import utils.utils as utils

from gpiozero import OutputDevice
from pump.carb import read_data_from_carb_pump

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

relay_pin = 27
relayCarbPump = OutputDevice(relay_pin)


def main():
    config = utils.read_config_file()
    
    if file_utils.run_file_checks():
        try:
            while True:                            
                # Turn on pump
                relayCarbPump.on()
                logging.info(f"Carb pump ON for {config['PUMP_ON_TIME']} seconds")
                time.sleep(config["PUMP_ON_TIME"])
                
                # Turn off pump
                relayCarbPump.off()
                logging.info(f"Carb pump OFF for {config['PUMP_OFF_TIME']} seconds")
                time.sleep(config["PUMP_OFF_TIME"])
                
                # TODO: Add support for standard pump data logging
        except Exception as e:
            logging.error(f"Error: {e}", exc_info=True)
        except KeyboardInterrupt:
            print("Interrupted by user. Shutting down.")
        finally:
            relayCarbPump.off()  # Ensure pump is off


if __name__ == "__main__":
    main()
