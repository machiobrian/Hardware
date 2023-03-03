# IoT Blink Project

from machine import Pin, Timer

led = Pin("LED", Pin.OUT)
timer = Timer()

def tick(timer):
    global led
    led.toggle()
    
timer.init(
    freq = 5.5,
    mode = Timer.PERIODIC,
    callback = tick
    )
