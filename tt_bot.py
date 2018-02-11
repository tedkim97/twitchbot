import string
import socket
import re
import time
import threading
from gen_functions import*
import chatreader as key
from tinder_wrapper import*

class Mode(Enum):
	ANARCHY = 1
	DEMOCRACY = 2

class tt_bot(object): 
	"""the chat bot is created as an object to give the flexibility
	of running multiple bots at once given different parameters"""

	def __init__(self,chan,iden,oauth,host="irc.chat.twitch.tv",port=6667): 
		self.CHANNEL = chan
		self.ID= iden
		self.PASS= oauth
		self.HOST= host
		self.PORT= port		
		self.readbuffer = ""
		self.socket = self._openSocket() 
		self._joinRoom()
		self.sendMessage("matchmakerbot MrDestructoid has connected ;)")

		self.running = True
		
		self.mode = Mode.DEMOCRACY
		self.tinder = tind_wrap()

		self.command_count = 0
		#self.tinder.state = States.CHATMENU #DONT forget to change this 
		
	def _joinRoom(self):
		joinRoom(self.socket, self.CHANNEL, self.readbuffer)

	def _openSocket(self):
		s = socket.socket()
		s.connect((self.HOST, self.PORT))
		encoded_send(s, "PASS " + self.PASS + "\r\n")
		encoded_send(s, "NICK " + self.ID + "\r\n")
		encoded_send(s, "JOIN #" + self.CHANNEL + "\r\n")
		return s

	def sendMessage(self, message): 
		sendMessage(self.socket, self.CHANNEL, message)

	def run(self): 
		#self.tinder.show_match_profile()
		while self.running: 
			self.readbuffer = self.readbuffer + (self.socket.recv(1024)).decode("utf-8")
			temp = self.readbuffer.split("\n")
			self.readbuffer = temp.pop()

			for line in temp: 
				#print(line)

				if "PING :tmi.twitch.tv" in line: 
					send_pong(self.socket)
					break

				user = getUser(line)
				message = getMessage(line)
				print(user + " typed: " + message)
				#print(message[0:])

				'''commands for the bot'''
				if ("terminate bot" in line) and (user == self.CHANNEL):
					print("terminating program")
					self.running = False
					self.sendMessage("terminating program")
					exit()
					break

				'''swipe commands'''
				if(("!right" in line) and ((self.tinder.get_state() == States.SWIPEMENU) or (self.tinder.get_state() == States.MATCHPROFILE))):
					print("someone voted right!")
					self.tinder.swipe_right()
					break

				if(("!left" in line) and ((self.tinder.get_state() == States.SWIPEMENU) or (self.tinder.get_state() == States.MATCHPROFILE))):
					print("someone voted left!")
					self.tinder.swipe_left()
					break

				if(("!superlike" in line) and ((self.tinder.get_state() == States.SWIPEMENU) or (self.tinder.get_state() == States.MATCHPROFILE))):
					print("someone super liked it")
					self.tinder.super_like()
					break

				if(("!go_chat" in line) and (self.tinder.get_state() == States.SWIPEMENU)):
					print("someone wanted to go to the chat menu")
					self.tinder.click_chat_menu()
					self.tinder.clear_search_and_move()
					break

				'''chat commands'''
				if(("!chat" in line) and (self.tinder.get_state() == States.CHATMENU)):
					print("CHAT REQUEST")
					self.tinder.search_person(message[6:])
					self.tinder.start_chat()
					break

				if(("!exitMSGS" in line) and (self.tinder.get_state() == States.CHATMENU)):
					print("exiting CHAT MENU")
					self.tinder.click_swipe_menu()
					break

				'''message commands'''
				if(("!sendmsg" in line) and (self.tinder.get_state() == States.CHATWINDOW)):
					print("Message Request")
					self.tinder.send_message(message[9:])
					break

				if(("!exitDM" in line) and (self.tinder.get_state() == States.CHATWINDOW)):
					print("Exitting DMs")
					self.tinder.exit_chat()
					self.tinder.clear_search()
					break

				'''vote commands'''
				if("!anarchy" in line):
					print("someone voted for anarchy")
					break

				if("!democracy" in line):
					print("someone vote democracy")
					break




if __name__ == "__main__": 
	#a = tc_bot("twitch_tries","bad_broker_bot","oauth:8298y40ehg7i3drbqjggqi49byztry")
	a = tt_bot(key.CHANNEL, key.IDENT,key.PASS)
	a.run()


