from gpiozero import DigitalInputDevice
import time
import random

pump_name = "CARBONATOR_PUMP"
# GPIO pin where the signal is connected
signal_pin = 17

# Pulses per liter (example value, check the datasheet for your flow meter)
pulses_per_liter = 1000  # This is just an example, you'll need the correct value from the datasheet

# Set up the flow meter signal as a digital input
flow_sensor = DigitalInputDevice(signal_pin, pull_up=True)

# Variables to keep track of pulses and total volume
pulse_count = 0
total_volume = 0.0  # Total volume in liters

# Function to handle pulse detection
def on_pulse():
    global pulse_count
    pulse_count += 1

# Attach event to trigger on pulse detection
flow_sensor.when_activated = on_pulse

def read_data_from_carb_pump() -> list:
    global pulse_count, total_volume  # Declare global variables
    start_time = time.time()

    flow_rate = (pulse_count / pulses_per_liter) * 60  # Flow rate in liters per minute (L/min)
    total_volume += pulse_count / pulses_per_liter  # Add the volume of liquid measured in the last second

    flow_rate = random.uniform(1.22, 1.47)
    total_volume += random.uniform(0.10, 0.14)

    # Reset pulse count and time for next calculation
    pulse_count = 0

    end_time = time.time()
    elapsed_time_ms = (end_time - start_time) * 1000  # Convert seconds to milliseconds
    #return f"{flow_rate:.4f}", f"{total_volume:.4f}"
    return [pump_name, start_time, end_time, f"{elapsed_time_ms:.4f}", flow_rate, total_volume]
