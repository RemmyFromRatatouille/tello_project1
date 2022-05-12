from djitellopy import tello
from time import sleep
# the 2 lines below will connect and set the tello to a name so, I have easy ref.
friend = tello.Tello()
friend.connect()
sleep(.5)

# prints the charge.
print(friend.get_battery())


# takes off and moves up 120cm (should be around 200cm or 6.6ft)
friend.takeoff()
friend.move_up(120)
sleep(2)

# moves to the bottem left of the room with 822cm moved & 3ft or 90cm of free room till it hits the walls.
friend.move_forward(500)
friend.move_forward(322)
sleep(1)

# rotates counter clock wise and moves 450cm to the bottom right of the room 90cm or 3ft of free space
friend.rotate_counter_clockwise(90)
friend.move_forward(450)
sleep(1)

# rotates and moves 822cm to the top right of the room, 90cm/3ft of space
friend.rotate_counter_clockwise(90)
friend.move_forward(500)
friend.move_forward(322)
sleep(1)

# rotates one last time moves 450cm to starting pos
friend.rotate_counter_clockwise(90)
friend.move_forward(450)
sleep(1)

# landing segment
friend.rotate_counter_clockwise(90)
friend.land()
