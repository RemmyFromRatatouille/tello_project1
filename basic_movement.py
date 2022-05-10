from djitellopy import tello
from time import sleep

friend = tello.Tello()
friend.connect()

print(friend.get_battery())
