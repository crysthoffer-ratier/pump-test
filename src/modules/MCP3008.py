from gpiozero import MCP3008, PWMOutputDevice

# Potentiometer connected to channel 0 of MCP3008
pot = MCP3008(channel=0)

# MOSFET Gate connected to GPIO18 (must support PWM!)
mosfet = PWMOutputDevice(18)

def get_potentiometer_value():
    mosfet.value = pot.value
    
    return pot.value