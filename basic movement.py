from djitellopy import tello
from time import sleep
chester = tello.Tello()
chester.connect()
print(chester.get_battery())
