from umodbus.serial import Serial
from umodbus.tcp import TCP
from network import WLAN
import machine

####################### TCP MODBUS #########################
WIFI_SSID = '_braen'
WIFI_PASS = 'Callmebr@3n'

wlan = WLAN(mode=WLAN.STA)
wlan.connect(WIFI_SSID, auth=(None, WIFI_PASS), timeout=5000)
while not wlan.isconnected():
    machine.idle() # save power while waiting

print('WLAN connection succeeded!')

slave_ip = 'slave ip'
modbus_obj = TCP(slave_ip)

slave_addr=0x0A
register_address=0x01
register_values=[2, -4, 6, -256, 1024]
signed=True

return_flag = modbus_obj.write_multiple_registers(slave_addr, register_address, register_values, signed)
output_flag = 'Success' if return_flag else 'Failure'
print('Writing multiple register status: ' + output_flag)