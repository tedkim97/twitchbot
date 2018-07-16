cimport string
import socket
import re
from gen_functions import*
import credentials as key

class base_bot: 
	'''This is a base-chat bot that has basic functionality of connecting
	to a chat of a specific channel, sending messages,and printing messages'''

	def __init__(self,channel,iden,oauth,host="irc.chat.twitch.tv",port=6667): 
		self.CHANNEL = channel
		self.ID= iden
		self.PASS= oauth
		self.HOST= host
		self.PORT= port			
		self.readbuffer = ""
		self.socket = openSocket(host,port,oauth,iden,channel)
		self._joinRoom()

	def _joinRoom(self):
		joinRoom(self.socket, self.CHANNEL, self.readbuffer)

	def chat(self, message): 
		sendMessage(self.socket, self.CHANNEL, message)

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
				print(user + " typed: " + message)

				if ("terminate bot" in line) and (user == self.CHANNEL):
					print("terminating program")
					self.sendMessage("terminating program")
					exit()
					break

if __name__ == "__main__": 
	a = base_bot(key.CHANNEL, key.IDENT,key.PASS)
	a.chat("HELLO HELLO")
	a.run()


