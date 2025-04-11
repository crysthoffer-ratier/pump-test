from gpiozero import OutputDevice,DigitalInputDevice
from time import sleep
import time

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' # orange on some systems
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'

RESET = '\033[0m' # called to return to standard terminal text color

# Set up the GPIO pin for controlling the relay
#relay = OutputDevice(27)

# GPIO pin where the signal is connected
signal_pin = 17

# Pulses per liter (example value, check the datasheet for your flow meter)
pulses_per_liter = 1000  # This is just an example, you'll need the correct value from the datasheet

# Set up the flow meter signal as a digital input
flow_sensor = DigitalInputDevice(signal_pin, pull_up=True)

# Variables to keep track of pulses and total volume
pulse_count = 0
total_volume = 0.0  # Total volume in liters
start_time = time.time()

# Function to handle pulse detection
def on_pulse():
    global pulse_count
    pulse_count += 1

# Attach event to trigger on pulse detection
flow_sensor.when_activated = on_pulse    

def test_no_stop():
    # Main loop to calculate flow rate and total volume
    try:
        
        
        while True:
            #relay.on()
            # Calculate elapsed time
            elapsed_time = time.time() - start_time
            
            # Every second, calculate the flow rate and total volume
            #if elapsed_time >= 1:
            flow_rate = (pulse_count / pulses_per_liter) * 60  # Flow rate in liters per minute (L/min)
            total_volume += pulse_count / pulses_per_liter  # Add the volume of liquid measured in the last second

            # Stop if the total volume is >= 0.14 liters
            #if total_volume >= 0.0014:
                #print("Total volume reached 0.14 liters. Stopping.")
                #break

            # Reset pulse count and time for next calculation
            pulse_count = 0
            start_time = time.time()

            # print(f"Flow Rate: {flow_rate:.4f} L/min")
            print(f"{BOLD}{BRIGHT_RED}Total Volume: {BRIGHT_GREEN}{total_volume:.4f} Liters")
            time.sleep(3)
            # Small delay to prevent CPU overloa
            #relay.off()
            time.sleep(2)
            total_volume = 0.0

    except KeyboardInterrupt:
        print("Program stopped.")
