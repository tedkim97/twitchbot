import string
import socket
import re
from gen_functions import*
import chatreader as key

class tc_bot(object): 
	"""the chat bot is created as an object to give the flexibility
	of running multiple bots at once given different parameters"""

	def __init__(self,chan,iden,oauth,host="irc.chat.twitch.tv",port=6667): 
		self.CHANNEL = chan
		self.ID= iden
		self.PASS= oauth
		self.HOST= host
		self.PORT= port		
		self.readbuffer = ""
		self.socket = self.openSocket() 
		self._joinRoom()

	def _joinRoom(self):
		joinRoom(self.socket, self.CHANNEL, self.readbuffer)

	def openSocket(self):
		s = socket.socket()
		s.connect((self.HOST, self.PORT))
		encoded_send(s, "PASS " + self.PASS + "\r\n")
		encoded_send(s, "NICK " + self.ID + "\r\n")
		encoded_send(s, "JOIN #" + self.CHANNEL + "\r\n")
		return s

	def sendMessage(self, message): 
		sendMessage(self.socket, self.CHANNEL, message)

	def run(self): 
		while True: 
			self.readbuffer = self.readbuffer + (self.socket.recv(1024)).decode("utf-8")
			temp = self.readbuffer.split("\n")
			self.readbuffer = temp.pop()

			for line in temp: 
				print(line)
				if "PING :tmi.twitch.tv" in line: 
					send_pong(self.socket)
					break

				user = getUser(line)
				message = getMessage(line)
				print(user + " typed: " + message)

				if ("terminate bot" in line) and (user == self.CHANNEL):
					print("terminating program")
					mod_func(self.socket, self.CHANNEL,'emote_only')
					#self.sendMessage("terminating program")
					#exit()
					break

				if("!right" in line):
					print("someone voted right!")

				if("!left" in line):
					print("someone voted left!")

				if("!superlike" in line):
					print("someone super liked it")


if __name__ == "__main__": 
	a = tc_bot(key.CHANNEL, key.IDENT,key.PASS)
	a.sendMessage("HELLO HELLO")
	a.run()


