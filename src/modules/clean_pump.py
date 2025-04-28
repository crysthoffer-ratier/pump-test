import time
from gpiozero import OutputDevice

relay_pin = 27
relayCarbPump = OutputDevice(relay_pin)

cleaning_time = 60

def main() -> None:
    try:
        print("PUMP ON!!!")
        relayCarbPump.on()

        for x in range(0, cleaning_time):
            print(f"==> {x}")
            
            time.sleep(1)
    except KeyboardInterrupt as exp:
        print("Bye bye!!!")
    finally:
        print("PUMP OFF!!!")
        relayCarbPump.off()


if __name__ == "__main__":
    main()
