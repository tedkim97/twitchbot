import string
import socket
import re
from gen_functions import*
#import pyautogui
#from keys import*
#from pynput import mouse as m 
#from pynput import keyboard as kb

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
		messageTemp = "PRIVMSG #" + self.CHANNEL + " :" + message
		encoded_send(self.socket, messageTemp+"\r\n")
		print("SENT: " + messageTemp)

	def run(self): 
		while True: 
			print("I dont think ")


if __name__ == "__main__": 
	a = tc_bot("twitch_tries","bad_broker_bot","oauth:8298y40ehg7i3drbqjggqi49byztry")
	a.sendMessage("HELLO HELLO")


