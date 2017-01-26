from network import WLAN, STA_IF
sta = WLAN(STA_IF)
sta.active(True)


# .scan() vracia list vsetkych pristupnych sieti
# pre kazu siet vrati tieto informavie (ssid, bssid, channel, RSSI, authmode, hidden)
# viac: http://docs.micropython.org/en/v1.8.2/esp8266/library/network.html?highlight=scan#network.wlan.scan

# Pre kazdu siet vypiseme jej meno (1. hodnota v zozname informacii)
for wifi in sta.scan():
    print(wifi[0])
