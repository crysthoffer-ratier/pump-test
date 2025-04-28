import time
import logging

from utils import misc, file_utils as file_utils, debug_utils as debug_utils

from gpiozero import OutputDevice
from pump.carb import monitor_flow_rate

relay_pin = 27
relayCarbPump = OutputDevice(relay_pin)


def relay_toggle(relay: OutputDevice) -> None:
    relay.toggle()


def test() -> None:
    try:
        if file_utils.run_file_checks():
            while True:
                relay_toggle(relayCarbPump)                
                
                carb_pump = monitor_flow_rate(duration=config["TEST"]["PUMP_ON_TIME"])

                relay_toggle(relayCarbPump)

                debug_utils.debug_message(carb_pump, logging.INFO)
                file_utils.append_to_file(carb_pump)
                
                time.sleep(config["TEST"]["PUMP_OFF_TIME"])
    except Exception as e:
        debug_utils.debug_message(e, logging.ERROR)


if __name__ == "__main__":
    config = misc.read_config_file()
    test()