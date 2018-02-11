import string
import socket
import re
import pyautogui as gui
from enum import Enum
import time


class States(Enum):
	SWIPEMENU = 1
	CHATMENU = 2
	PROFILEMENU = 3 
	MATCHPROFILE = 4
	CHATWINDOW = 5
	MATCHMADE = 6

class tind_wrap(object):
	state = States.SWIPEMENU
	def __init__(self):
		self.state = States.SWIPEMENU

	def get_state(self):
		return self.state

	def change_state(self, dst:States):
		'''Function that sorta became useless oops'''
		self.state = dst
		print(self.state)
	'''menu commands'''
	def click_swipe_menu(self):
		self.state = States.SWIPEMENU
		gui.moveTo(965,110, duration = 0.01)
		gui.click()
		#gui.click(x = 774, y = 94)

	def click_chat_menu(self):
		self.state = States.CHATMENU
		gui.moveTo(1130,110, duration =0.01)
		gui.click()
		time.sleep(0.02)
		self.clear_search()
		#gui.click(x=909,y=92)

	def click_profile_menu(self):
		self.state = States.PROFILEMENU
		gui.moveTo(800,110, duration =0.01)
		gui.click()
		#gui.click(x=643,y=94)

	'''swipe menu commands'''
	def show_match_profile(self):
		if(self.state == States.SWIPEMENU or self.state == States.MATCHPROFILE):
			gui.moveTo(1150,823,duration=0.01)
			gui.click()
			self.state = States.MATCHPROFILE
		else: 
			print("cannot show profile because we are not in the swipe menu")

	def hide_profile(self):
		if(self.state == States.MATCHPROFILE):
			gui.moveTo(1183,587,duration=0.01)
			gui.click(clicks=2)
			print(self.state)
			self.state = States.SWIPEMENU
			print(self.state)
		else:
			print("cannot hide profile because we are not in the match's profile")


	def pic_right(self):
		if(self.state == States.SWIPEMENU or self.state == States.MATCHPROFILE):
			gui.moveTo(1040,500, duration =0.01)
			gui.click()
		else:
			print("not in swipe menu: cannot use swipe")
	
	def pic_left(self):
		if(self.state == States.SWIPEMENU or self.state == States.MATCHPROFILE):
			gui.moveTo(800,500, duration =0.01)
			gui.click()
		else:
			print("not in swipe menu: cannot use swipe")	

	def swipe_right(self):
		if(self.state == States.SWIPEMENU or self.state == States.MATCHPROFILE):
			gui.moveTo(1040,923, duration =0.01)
			gui.click()
			# gui.moveto(965,587)
			# gui.click()
			# self.show_match_profile()
		else:
			print("not in swipe menu: cannot use swipe")

	def swipe_left(self):
		if(self.state == States.SWIPEMENU or self.state == States.MATCHPROFILE):
			gui.moveTo(890,923,duration = 0.01)
			gui.click()
			# self.show_match_profile()
		else:
			print("not in swipe menu: cannot use swipe")

	def super_like(self):
		if(self.state == States.SWIPEMENU or self.state == States.MATCHPROFILE):
			gui.moveTo(965,923,duration = 0.01)
			# gui.click()
			# self.show_match_profile()
		else:
			print("not in swipe menu: cannot superlike")

	def rewind(self):
		if(self.state == States.SWIPEMENU):
			gui.moveTo(815,923,duration = 0.01)
			gui.click()
		else:
			print("not in swipe menu: cannot rewind")

	def skip_the_line(self): 
		if(self.state == States.SWIPEMENU):
			gui.moveTo(1115,923,duration = 0.01)
			gui.click()
		else:
			print("not in swipe menu: cannot skip_the_line")


	'''chat menu commands'''
	def search_person(self, name:str):
		if(self.state == States.CHATMENU):
			gui.moveTo(965,165, duration=0.1)
			gui.click()
			gui.typewrite(name, interval = 0.05)
			time.sleep(0.05)
			#gui.typewrite("hiii ;)", interval = 0.25)
		else:
			print("not in chat menu: cannot message_person")

	def clear_search(self):
		if(self.state == States.CHATMENU):
			gui.moveTo(1200,165, duration=0.1)
			gui.click()
		else:
			print("not in chat menu: cannot clear_search")

	def clear_search_and_move(self):
		if(self.state == States.CHATMENU):
			gui.moveTo(1200,165, duration=0.1)
			gui.click()
			gui.moveTo(1200,210, duration=0.1)
			gui.click()
		else:
			print("not in chat menu: cannot clear_search")

	def start_chat(self):
		'''this function is NOT going to be smart because i'm out 
		of time :('''
		if(self.state == States.CHATMENU):
			gui.moveTo(845, 255, duration=0.1)
			gui.click()
			time.sleep(0.5)
			gui.moveTo(847,425, duration=0.1)
			gui.click()
			time.sleep(0.5)
			self.state = States.CHATWINDOW
		else:
			print("not in chat menu: cannot start_chat")

	def exit_chat(self):
		if(self.state == States.CHATWINDOW):
			gui.moveTo(748,114)
			gui.click()
			self.state = States.CHATMENU
		else:
			print("not in chat windows: cannot exit_char(window)")

	def send_message(self, message:str):
		if(self.state == States.CHATWINDOW):
			gui.moveTo(1040,950, duration=0.1)
			gui.click()
			time.sleep(0.05)
			gui.typewrite(message,interval = 0.05)
			gui.moveTo(1200,950, duration=0.1)
			gui.click()
		else:
			print("not in chat window: cannot send message")

if __name__ == "__main__": 
	a = tind_wrap()
	time.sleep(3)
	a.click_chat_menu()
	time.sleep(1)
	a.click_profile_menu()
	time.sleep(1)
	a.click_swipe_menu()
	#a.swipe_right()
	a.swipe_left()
	time.sleep(1)
	a.swipe_left()
	time.sleep(1)
	#a.rewind()
	#a.skip_the_line()
	a.pic_right()
	a.pic_right()
	a.pic_left()
	# a.show_match_profile()
	# time.sleep(0.5)
	# a.hide_profile()
	# a.swipe_left()


	#a.super_like()

	# a.click_chat_menu()
	# time.sleep(0.5)
	# a.search_person("liz")
	# time.sleep(0.5)
	# a.clear_search()
	# time.sleep(0.5)
	# a.search_person("Dominique")
	# time.sleep(0.5)
	# a.start_chat()
	# time.sleep(0.5)
	# #a.exit_chat()
	# a.send_message("My name is Kenneth")
	# for x in range(0,50):
	# 	print(x)
	# 	a.swipe_right()


