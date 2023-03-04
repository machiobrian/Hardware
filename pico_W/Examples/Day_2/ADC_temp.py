import machine
import utime 

sensor_temp = machine.ADC(4) # defined ADC channel by "channel"
# sensor_temp = machine.ADC() # defined by pin number : fifth ADC input

conversion_factor = 3.3 / (65535)

while True:
    reading = sensor_temp.read_u16() * conversion_factor

    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    utime.sleep(1)