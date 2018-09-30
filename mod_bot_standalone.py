import string
import socket
import re
from gen_functions import*
from keys import credentials as key

class mod_bot(object): 
	"""the mod-bot is created as an object to give the flexibility
	of running multiple bots at once given different parameters"""


	###FIX HOW WE GET THESE FILE NAMES LATER
	def __init__(self,chan,iden,oauth,resp_fname='configs/bot_responses.txt',
				ban_fname='configs/ban_responses.txt',
				host="irc.chat.twitch.tv",port=6667): 
		self.CHANNEL = chan
		self.ID= iden
		self.PASS= oauth
		self.HOST= host
		self.PORT= port		
		self.readbuffer = ""
		self.resp_tab = unpack_response(resp_fname)
		self.mod_resp_tab = unpack_response(ban_fname)
		self.ztest = {**self.resp_tab, **self.mod_resp_tab}
		self.socket = openSocket(host,port,oauth,iden,chan)
		self._joinRoom()

	def _joinRoom(self):
		joinRoom(self.socket, self.CHANNEL, self.readbuffer)

	#Still debating whether I want to keep this modified function here - 
	# it doesn't really add anything significant to the program 
	def openSocket(self):
		s = socket.socket()
		s.connect((self.HOST, self.PORT))
		encoded_send(s, "PASS " + self.PASS + "\r\n")
		encoded_send(s, "NICK " + self.ID + "\r\n")
		encoded_send(s, "JOIN #" + self.CHANNEL + "\r\n")
		return s

	def chat(self, message, user=""):
		if user == "": 
			sendMessage(self.socket, self.CHANNEL, message)
		else: 
			#this sends out whispers in twitchchat
			new_message = "/w " + user + " " + message
			sendMessage(self.socket, self.CHANNEL, new_message)

	def mod_func(self, func, user ='', time=0, ban_msg = ''):
		mod_func(self.socket, self.CHANNEL, func, user = user, time = time, ban_msg = ban_msg)

	def run(self): 
		while True: 
			self.readbuffer = self.readbuffer + (self.socket.recv(1024)).decode("utf-8")
			temp = self.readbuffer.split("\n")
			self.readbuffer = temp.pop()

			for line in temp: 
				if "PING :tmi.twitch.tv" in line: 
					send_pong(self.socket)
					break

				user = getUser(line)
				message = getMessage(line)

				b = auto_resp_msg(self.mod_resp_tab, message)
				if(b != ""):
					self.mod_func(b, user = user, time = 3)

				a = auto_resp_msg(self.resp_tab, message)			
				if(a != ""):	
					self.chat(a, user = user)

				print(user + " typed: " + message)

				if ("terminate bot" in line) and (user == self.CHANNEL):
					print("terminating program")
					self.chat("terminating program",user = self.CHANNEL)
					sendMessage("terminating program")
					exit()
					break

if __name__ == "__main__": 
	a = mod_bot(key.CHANNEL, key.IDENT,key.PASS)
	# a.chat("Mod_Bot has started", user = key.CHANNEL)
	a.chat("Why isn't this wokring??")
	a.run()

