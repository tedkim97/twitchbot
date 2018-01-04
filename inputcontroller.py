from pynput import mouse as m
from pynput import keyboard as kb


mouse = m.Controller()
keyboard = kb.Controller()

def pressKey(keyb, k: str): 
	keyb.press(k)
	keyb.release(k)


def leftClick(mos): 
	mos.press(m.Button.left)
	mos.release(m.Button.left)

def makeWorker(key):
	pressKey(keyboard, '5')
	pressKey(keyboard, 's')

def selectArmy(): 
	pressKey('1')

if __name__ == "__main__": 
	while True: 		
		print("hello")
		#pressKey(keyboard, "1")
		#leftClick(mouse)

		'''
		mouse.press(m.Button.left)
		mouse.release(m.Button.left)
		'''
