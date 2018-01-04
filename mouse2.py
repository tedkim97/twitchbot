from pynput.mouse import Button, Controller
import time

mouse = Controller() 

while True:
	print('The current pointer posiiton is {0}'.format(mouse.position))
	time.sleep(2)
	mouse.press(Button.left)
	mouse.move(-200, 200)
	time.sleep(2)
	mouse.release(Button.left)

'''
time.sleep(5)

mouse.position = (800, 200)
print("Now it's at {0}".format(mouse.position))
time.sleep(5)

mouse.move(5, -5)
print("now we moved it a bit")
time.sleep(5)

mouse.press(Button.left)
mouse.release(Button.left)

mouse.scroll(0,2)


while True: 
	mouse.move(0,5)
	print(mouse.position)
	x,y = mouse.position 
	if y > 700: 
		break 
'''