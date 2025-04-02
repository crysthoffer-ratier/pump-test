from gpiozero import DigitalInputDevice
import time

# GPIO pin where the signal is connected
signal_pin = 17

# Pulses per liter (example value, check the datasheet for your flow meter)
# pulses_per_liter = 1700  # This is just an example, you'll need the correct value from the datasheet
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

# Main loop to calculate flow rate and total volume
start_time2 = int(time.time())
try:
    while True:
        # Calculate elapsed time
        elapsed_time = time.time() - start_time
        
        # Every second, calculate the flow rate and total volume
        if elapsed_time >= 1:
            flow_rate = (pulse_count / pulses_per_liter) * 60  # Flow rate in liters per minute (L/min)
            total_volume += pulse_count / pulses_per_liter  # Add the volume of liquid measured in the last second

            stop_time = time.time()
            print(f"Flow Rate: {flow_rate:.4f} L/min")
            print(f"Total Volume: {total_volume:.4f} Liters")

            # Reset pulse count and time for next calculation
            pulse_count = 0
            start_time = time.time()
        
        time.sleep(0.1)  # Small delay to prevent CPU overload

except KeyboardInterrupt:
    print("Program stopped.")
    print(f"Start time: {int(start_time2)}")
    print(f"Stop time: {int(stop_time)}")
