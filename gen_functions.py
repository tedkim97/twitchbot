import string
import socket
import re

def encoded_send(socket, msg:str):
	socket.send(msg.encode("utf-8"))

def getMessage(line): 
	separate = line.split(":", 2)
	message = separate[2]
	return message

def getUser(line):
	separate = line.split(":", 2)
	user = separate[1].split("!", 1)[0]
	return user 

def sendMessage(socket, channel, message): 
	messageTemp = "PRIVMSG #" + channel + " :" + message
	encoded_send(socket, messageTemp+"\r\n")
	print("SENT: " + messageTemp)

def joinRoom(socket, channel, readbuffer):
	Loading = True 
	while Loading: 
		readbuffer= readbuffer + (socket.recv(1024)).decode("utf-8")
		temp= readbuffer.split("\n")
		readbuffer= temp.pop()

		for line in temp: 
			print(line)
			Loading = loadingComplete(line)
	sendMessage(socket, channel ,"joined chat")

def loadingComplete(line): 
	if("End of /NAMES list" in line): 
		return False 
	return True 

def timeout(s, user, time=60): 
	sendMessage(s, "/timeout {} {}".format(user,str(time)))

def ban(s, user): 
	sendMessage(s, "/ban {}".format(user))

def unban(s, user): 
	sendMessage(s, "/unban {}".format(user))

def followers_only(s, length: str):
	sendMessage(s, "/followers {}".format(length))

def followers_off(s):
	sendMessage(s, "/followersoff")

def slowmode(s, time=60): 
	sendMessage(s, "/slow" + str(time))

def slow_off(s): 
	sendMessage(s, "/slowoff")

def emote_only(s): 
	sendMessage(s, "/emoteonly")

def emote_off(s): 
	sendMessage(s, "/emoteonlyoff")

def send_pong(s): 
	encoded_send(s, "PONG :tmi.twitch.tv\r\n")
	print("PONG sent to twitch")