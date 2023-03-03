from machine import Pin, Timer
import time

led = Pin("LED",Pin.OUT)
timer  = Timer(0)
toggle = 1 

def blink(timer):
    global toggle

    if toggle == 1:
        led.value(0)
        toggle = 0

    else:
        led.value(1)
        toggle = 1

    timer.init(
        freq=6,
        mode=Timer.PERIODIC,
        callback = blink
    )