import string
import socket
import re
import pyautogui
from keys import*
from pynput import mouse as m 
from pynput import keyboard as kb

class tc_bot(object): 
	"""the chat bot is created as an object because I want to have the option 
	of running multiple bots at once given different parameters"""

	def __init__(self,chan,iden,oauth,host="irc.chat.twitch.tv",port=6667): 
		HOST= host
		PORT= port
		ID= iden
		PASS= pw
		readbuffer = ""
		s = openSocket()

	def encoded_send(self,socket,msg:str):
		socket.send(msg.encode("utf-8"))

	def joinRoom(self, socket):
		Loading = True 
		while Loading: 
			self.readbuffer= self.readbuffer + (s.recv(1024)).decode("utf-8")
			temp= readbuffer.split("\n")
			readbugger= temp.pop()

			for line in temp: 
				print(line)
				Loading = loadgincComplete(line)
		sendMessage(s, "joined chat")

	def loadingComplete(self, line): 
		if("End of /NAMES list" in line): 
			return False 
		return True 


	def openSocket(self):
		s = socket.socket()
		s.connect((HOST, PORT))




