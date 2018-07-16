import string
import socket
import re

'''Essential functions for connecting to and interacting with'''
def encoded_send(socket, msg:str):
	'''passes a properly encoded message to the socket'''
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

def loadingComplete(line): 
	if("End of /NAMES list" in line): 
		return False 
	return True 

def send_pong(socket): 
	encoded_send(socket, "PONG :tmi.twitch.tv\r\n")
	#not necessary, but gives confirmation that the pong is working properly
	print("PONG sent to twitch") 

def openSocket(host, port, pass_w, nick_n, channel):
	s = socket.socket()
	s.connect((host, port))
	encoded_send(s, "PASS " + pass_w + "\r\n")
	encoded_send(s, "NICK " + nick_n + "\r\n")
	encoded_send(s, "JOIN #" + channel + "\r\n")
	return s

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

#match function

#Moderator/Broadcaster Functions
def mod_func(socket, channel, func, user ='', time=0, ban_msg = ''):
	'''time is measured in minutes'''
	if (time == 0) and ((func == 'timeout_user') or (func == 'slowmode')):
		time = ""
	

	#This IF lets the bot avoid spamming useless commands
	if (user == '') and ((func == 'timeout_user') or (func == 'unban_user') or 
	(func == 'ban_user')):
		print("Invald Mod Function")
		return

	switcher = {
		'timeout_user': "/timeout {} {}".format(user, str(60 * time)),
		'ban_user': "/ban {} {}".format(user, ban_msg),
		'unban_user': "/unban {}".format(user),
		'followers_only': "/followers {}".format(time),
		'followers_off': "/followersoff",
		'slowmode': "/slow {}".format(time),
		'slow_off': "/slowoff",
		'emote_only': "/emoteonly",
		'emote_off': "/emoteonlyoff"
	}
	execute = switcher.get(func, "E R R O R")
	sendMessage(socket, channel, execute)
