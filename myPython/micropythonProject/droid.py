from machine import Pin
def light_state():
    led = Pin(25, Pin.OUT)
    led.value(1)
    led.toggle()
