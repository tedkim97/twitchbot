import pyautogui
import re 

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = False

width, height = pyautogui.size()


for i in range(10): 
	#pyautogui.moveTo(100, 100, duration = 0.25)
	#pyautogui.moveTo(200, 100, duration = 0.25)
	#pyautogui.moveTo(200, 200, duration = 0.25)
	#pyautogui.moveTo(100, 200, duration = 0.25)
	pyautogui.moveTo(100, 100, duration = 0.01)
	pyautogui.moveTo(200, 100, duration = 0.01)
	pyautogui.moveTo(200, 200, duration = 0.01)
	pyautogui.moveTo(100, 200, duration = 0.01)

#while True: 
#	print(pyautogui.position())

#pyautogui.click(500, 500)
#pyautogui.typewrite("Fuck you")

'''
while True: 
	x,y  = pyautogui.position()
	pyautogui.moveTo(x+30, y+30, duration = 0.25)
'''

p = re.compile('!\S+')
a = p.match("!HELLO")
b = p.match("ABC")
c = p.match("!BUY")

#print(a.group())
print(a)
#b.group()
print(c.group())

p2 = re.compile('^!\w+\s+\S+')
a2 = p2.match("!BUY   AMD")
print(a2.group())

a3 = re.match('^!\w+\s+\S+', "!BUY  APPL")
print(a3.group())