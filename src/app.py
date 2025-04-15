import time
import logging

from utils import misc, file_utils as file_utils, debug_utils as debug_utils

from gpiozero import OutputDevice
from pump.carb import read_data_from_carb_pump

relay_pin = 27
relayCarbPump = OutputDevice(relay_pin)

def main():
    config = misc.read_config_file()
    
    if file_utils.run_file_checks():
        try:
            while True:                            
                # Turn on pump
                relayCarbPump.on()
                debug_utils.debug_message(f"Carb pump ON for {config['PROD']['PUMP_ON_TIME']} seconds", logging.INFO)            

                time.sleep(config["PROD"]["PUMP_ON_TIME"])
                
                pump = read_data_from_carb_pump()

                file_utils.append_to_file(pump)

                # Turn off pump
                relayCarbPump.off()
                debug_utils.debug_message(f"Carb pump ON for {config['PROD']['PUMP_OFF_TIME']} seconds", logging.INFO)
                time.sleep(config["PROD"]["PUMP_OFF_TIME"])
                
                # TODO: Add support for standard pump data logging
        except Exception as e:
            logging.error(f"Error: {e}", exc_info=True)
        except KeyboardInterrupt:
            print("Interrupted by user. Shutting down.")
        finally:
            relayCarbPump.off()  # Ensure pump is off


if __name__ == "__main__":
    main()
