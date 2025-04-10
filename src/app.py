import time
from gpiozero import OutputDevice
import utils.file_utils as file_utils

from pump.carb import read_data_from_carb_pump
from pump.standard import read_data_from_standard_pump

relay_pin = 27
relayCarbPump = OutputDevice(relay_pin)

def main():
    if file_utils.run_file_checks():
        while True:
            try:
                relayCarbPump.on()
                pump1 = read_data_from_carb_pump()
                time.sleep(3)
                
                relayCarbPump.off()
                time.sleep(2)

                #file_utils.append_to_file(pump1)
            except Exception as e:
                print(e)
            
            # pump2 = read_data_from_standard_pump()            
            # file_utils.append_to_file(pump2)


if __name__ == "__main__":
    main()
