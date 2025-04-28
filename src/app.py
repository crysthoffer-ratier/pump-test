import time
import logging

from utils import misc, file_utils as file_utils, debug_utils as debug_utils

from gpiozero import OutputDevice
from pump.carb import monitor_flow_rate

relay_pin = 27
relayCarbPump = OutputDevice(relay_pin)


def relay_toggle(relay: OutputDevice) -> None:
    relay.toggle()


def main() -> None:
    aq_pump = "AQUATEC_PUMP"
    aq_pump_ppl = config["PROD"]["AQUATEC_PUMP"]

    ca_pump = "CHARLES_AUSTEN_PUMP"
    ca_pump_ppl = config["PROD"]["CHARLES_AUSTEN_PUMP"]
    try:
        if file_utils.run_file_checks():
            while True:
                relay_toggle(relayCarbPump)                
                
                # ca_pump_data = monitor_flow_rate(pulses_per_liter=aq_pump_ppl, pump=ca_pump, duration=config["PROD"]["PUMP_ON_TIME"])
                ca_pump_data = monitor_flow_rate(pulses_per_liter=ca_pump_ppl, pump=ca_pump, duration=config["PROD"]["PUMP_ON_TIME"])

                relay_toggle(relayCarbPump)

                #debug_utils.debug_message(aq_pump_data, logging.INFO)
                #file_utils.append_to_file(aq_pump_data)

                debug_utils.debug_message(ca_pump_data, logging.INFO)                
                file_utils.append_to_file(ca_pump_data)
                
                time.sleep(config["PROD"]["PUMP_OFF_TIME"])
    except Exception as e:
        debug_utils.debug_message(e, logging.ERROR)


if __name__ == "__main__":
    config = misc.read_config_file()
    main()