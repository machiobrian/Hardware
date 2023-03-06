# implementing I2C

from machine import Pin, I2C

# we construct and return I2C objects using the params below
i2c = I2C(
    0, 
    scl=Pin(9),
    sda=Pin(8),
    freq=400000
)

# 0: identifies a particular i2c peripheral

i2c.scan() # scan addressed btn 0x08 and 0x77 and return a list of those that respond
i2c.writeto(12, b"123")
i2c.readfrom(12, 4)


i2c = I2C(
    1,
    scl=Pin(7),
    sda=Pin(6),
    freq=400000
)
i2c.scan()
i2c.writeto_mem(12,6,b'456')
i2c.readfrom_mem(12,6,4)