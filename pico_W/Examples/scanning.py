# 2.4 GHz WiFi

# Scan all available Network Access Points

import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

access_points = wlan.scan()

for access_point in access_points:
    print(access_point)