import string
import socket
import re


'''Essential functions'''
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

def loadingComplete(line): 
	if("End of /NAMES list" in line): 
		return False 
	return True 

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


#Moderator/Broadcaster Functions
def timeout(socket, channel, user, time=60): 
	sendMessage(socket, channel, "/timeout {} {}".format(user,str(time)))

def ban(socket, channel,user): 
	sendMessage(socket, channel,"/ban {}".format(user))

def unban(socket, channel,user): 
	sendMessage(socket, channel,"/unban {}".format(user))

def followers_only(socket, channel,length: str):
	'''Followers only takes a very specific format: 
	#m = #minutes
	#h = #hours
	#d = #days
	#w = #weeks
	#mo = #months'''
	sendMessage(socket,channel, "/followers {}".format(length))

def followers_off(socket,channel):
	sendMessage(socket, channel, "/followersoff")

def slowmode(socket, channel,time=60): 
	sendMessage(socket, channel, "/slow" + str(time))

def slow_off(socket, channel): 
	sendMessage(socket, channel,"/slowoff")

def emote_only(socket,channel): 
	sendMessage(socket, channel, "/emoteonly")

def emote_off(socket,channel): 
	sendMessage(socket,channel,"/emoteonlyoff")

def send_pong(socket): 
	encoded_send(socket, "PONG :tmi.twitch.tv\r\n")
	print("PONG sent to twitch")

#Definitely does not work
# def mod_func(socket, channel, func, *additional_param):
# 	#'timeout': 
# 	#'ban':
# 	#'unban':
# 	{
# 		'followers_only': followers_only(socket,channel, "10m"),
# 		'followers_off': followers_off(socket,channel),
# 		'slowmode': slowmode(socket,channel),
# 		'slow_off': slow_off(socket,channel),
# 		'emote_only': emote_only(socket,channel),
# 		'emote_off': emote_off(socket,channel)
# 	}[func]
# 	print("Done")

def mod_func(socket, channel, func, user ="", time=0):
	if time == 0: 
		t_length = ""

	switcher = {
		'timeout_user': "/timeout {} {}".format(user, str(60 * time)),
		'ban_user': "/ban {}".format(user),
		'unban_user': "/unban {}".format(user),
		'followers_only': ("/followers {}".format(time)),
		'followers_off': "/followersoff",
		'slowmode': ("/slow {}".format(time)),
		'slow_off': ("/slowoff"),
		'emote_only': "/emoteonly",
		'emote_off': "/emoteonlyoff"
	}
	execute = switcher.get(func, "E R R O R")
	sendMessage(socket, channel, execute)
