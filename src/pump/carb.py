import time

from typing import Any
from collections import deque
from gpiozero import OutputDevice, MCP3008, PWMOutputDevice, DigitalInputDevice

# GPIO pin where the signal is connected
signal_pin = 17

# Pulses per liter (example value, check the datasheet for your flow meter)
# pulses_per_liter = 820  # This is just an example, you'll need the correct value from the datasheet

# Set up the flow meter signal as a digital input
flow_sensor = DigitalInputDevice(signal_pin, pull_up=True)

# Variables to keep track of pulses and total volume
pulse_count = 0
total_volume = 0.0  # Total volume in liters

# Function to handle pulse detection
def on_pulse():
    global pulse_count
    pulse_count += 1
    # print(f"Pulse: {pulse_count}")

# Attach event to trigger on pulse detection
flow_sensor.when_activated = on_pulse

def monitor_flow_rate(pulses_per_liter:int, pump: str, duration: Any = 1) -> list:
    global pulse_count, total_volume

    pulse_count = 0  # Reset before measuring
    start_time = time.time()

    time.sleep(duration)  # Collect pulses for 'duration' seconds

    end_time = time.time()
    elapsed_time = end_time - start_time

    flow_rate = (pulse_count / pulses_per_liter) / elapsed_time * 60  # L/min
    volume = pulse_count / pulses_per_liter
    total_volume += volume

    return [pump, int(start_time), int(end_time), f"{elapsed_time*1000:.2f}", f"{flow_rate:.3f}", f"{volume:.3f}", f"{total_volume:.3f}"]