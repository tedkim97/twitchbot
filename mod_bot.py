import string
import socket
import re
from gen_functions import*
import chatreader as key
from base_bot import base_bot

class mod_bot(base_bot): 
	"""the mod-bot is created as an object to give the flexibility
	of running multiple bots at once given different parameters"""

	def __init__(self,chan,iden,oauth,host="irc.chat.twitch.tv",port=6667): 
		base_bot.__init__(self,chan,iden,oauth,host,port)

	def chat(self, message): 
		base_bot.chat(self,message)

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
					mod_func(self.socket, self.CHANNEL,'emote_only')
					#self.sendMessage("terminating program")
					#exit()
					break


if __name__ == "__main__": 
	a = mod_bot(key.CHANNEL, key.IDENT,key.PASS)
	a.chat("HELLO HELLO")
	a.run()


