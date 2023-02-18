import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect("_braen", "Callmebr@3n")
print(wlan.isconnected())