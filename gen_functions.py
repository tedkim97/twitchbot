import string
import socket
import re

def encoded_send(socket, msg:str):
	socket.send(msg.encode("utf-8"))

def getMessage(self, message): 
	separate = line.split(":", 2)
	message = separate[2]
	return message

def getUser(line):
	separate = line.split(":", 2)
	user = separate[1].split("!", 1)[0]
	return user 

def sendMessage(socket, message): 
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	encoded_send(socket, messageTemp+"\r\n")
	print("SENT: " + messageTemp)

def joinRoom(socket, readbuffer):
	Loading = True 
	while Loading: 
		readbuffer= readbuffer + (socket.recv(1024)).decode("utf-8")
		temp= readbuffer.split("\n")
		readbuffer= temp.pop()

		for line in temp: 
			print(line)
			Loading = loadingComplete(line)
	sendMessage("joined chat")

def loadingComplete(line): 
	if("End of /NAMES list" in line): 
		return False 
	return True 