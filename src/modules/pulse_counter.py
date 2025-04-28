import time
from gpiozero import DigitalInputDevice, OutputDevice

relay_pin = 27
relayCarbPump = OutputDevice(relay_pin)

signal_pin = 17
flow_sensor = DigitalInputDevice(signal_pin, pull_up=True)

pulse_count = 0

def on_pulse():
    global pulse_count
    pulse_count += 1

flow_sensor.when_activated = on_pulse

def count_pulses(duration_sec=60):
    global pulse_count

    pulse_count = 0
    relayCarbPump.on()
    time.sleep(1)  # Optional: stabilize pump

    print("Counting pulses...")
    start_time = time.time()
    time.sleep(duration_sec)
    end_time = time.time()

    elapsed = end_time - start_time
    relayCarbPump.off()

    print(f"Total pulses in {elapsed:.1f} seconds: {pulse_count}")

    flow_sensor.close()

if __name__ == '__main__':
    try:
        count_pulses()
    except KeyboardInterrupt:
        relayCarbPump.off()
        flow_sensor.close()
