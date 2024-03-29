# enabling RELP over UART
from machine import Pin

p2 = Pin(2, Pin.IN, Pin.PULL_UP)
p2.irq(
    lambda pin: print("IRQ with Flags: ", pin.irq().flags()),
    Pin.IRQ_FALLING
)