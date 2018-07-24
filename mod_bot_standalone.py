import string
import socket
import re
from gen_functions import*
from redundant import credentials as key

class mod_bot(object): 
	"""the mod-bot is created as an object to give the flexibility
	of running multiple bots at once given different parameters"""

	def __init__(self,chan,iden,oauth,host="irc.chat.twitch.tv",port=6667): 
		self.CHANNEL = chan
		self.ID= iden
		self.PASS= oauth
		self.HOST= host
		self.PORT= port		
		self.readbuffer = ""
		self.socket = openSocket(host,port,oauth,iden,chan)
		self._joinRoom()
		self.resp_tab = message_response('bot_responses.txt')

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

	def run(self): 
		while True: 
			self.readbuffer = self.readbuffer + (self.socket.recv(1024)).decode("utf-8")
			temp = self.readbuffer.split("\n")
			self.readbuffer = temp.pop()

			for line in temp: 
				if "PING :tmi.twitch.tv" in line: 
					print("Ping received") # not necessary
					send_pong(self.socket)
					break

					

				user = getUser(line)
				message = getMessage(line)

				a = auto_resp_msg(self.resp_tab, message)			
				if(a != ""):
					# self.chat(a)
					self.chat(a, user = user)

				print(user + " typed: " + message)

				if ("terminate bot" in line) and (user == self.CHANNEL):
					print("terminating program")
					self.chat("terminating program",user = self.CHANNEL)
					# sendMessage("terminating program")
					exit()
					break

				if ("tf" in line) and (user == self.CHANNEL):
					print("Testing Function")
					#mod_func(self.socket, self.CHANNEL,'emote_only') #works
					#mod_func(self.socket, self.CHANNEL, 'timeout_user', 'twitch_tries', time=5)
					#mod_func(self.socket, self.CHANNEL, 'unban_user', 'twitch_tries')
					#mod_func(self.socket, self.CHANNEL, 'timeout_user', 'twitch_tries',time=1)
					# mod_func(self.socket, self.CHANNEL, 'timeout_user') #works
					# mod_func(self.socket, self.CHANNEL, 'ban_user') #works
					# mod_func(self.socket, self.CHANNEL, 'unban_user') #works
					#mod_func(self.socket, self.CHANNEL, 'slowmode', time=5) #works
					#mod_func(self.socket, self.CHANNEL, 'slowmode')


if __name__ == "__main__": 
	a = mod_bot(key.CHANNEL, key.IDENT,key.PASS) # #'imaqtpie'
	#a.chat("HELLO HELLO")
	a.run()

