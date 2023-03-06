from machine import SPI

spi = SPI(0)
spi = SPI(0, 100_000) # baudrate
spi = SPI(
    0,
    100_000,
    polarity=1,
    phase=1 
) # phase: trailing, pol = active high

spi.write('test')
spi.read(5)

buf = bytearray(3) # create a mutable byte array object
spi.write_readinto('out', buf)
