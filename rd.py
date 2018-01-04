import string
import socket
import re
import pyautogui
from keys import*
from pynput import mouse as m 
from pynput import keyboard as kb

#CHANNEL = "twitchwritesmyessay"
CHANNEL = "twitch_tries"

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = False

commands = []

def encoded_send(sock, msg: str):
	sock.send(msg.encode("utf-8"))

def moveMouse(dist: int, dir: str): 
	if dir == "UP": 
		pyautogui.moveRel(0, -dist, duration =0.25)
	elif dir == "DOWN": 
		pyautogui.moveRel(0, dist, duration =0.25)
	elif dir == "LEFT":
		pyautogui.moveRel(-dist, 0, duration=0.25)
	elif dir == "RIGHT":
		pyautogui.moveRel(dist, 0, duration=0.25)
	else: 
		raise ValueError("invalid direction")

def getUser(line): 
	separate = line.split(":", 2)
	user = separate[1].split("!", 1)[0]
	return user 

def getMessage(line): 
	separate = line.split(":", 2)
	message = separate[2]
	return message

def openSocket(): 
	s = socket.socket()
	s.connect((HOST, PORT))
	encoded_send(s, "PASS " + PASS + "\r\n")
	encoded_send(s, "NICK " + IDENT + "\r\n")
	encoded_send(s, "JOIN #" + CHANNEL + "\r\n")
	return s

def sendMessage(s, message): 
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	encoded_send(s, messageTemp+"\r\n")
	print("Sent: " + messageTemp)

def joinRoom(s): 
	readbuffer = ""
	Loading = True
	while Loading: 
		readbuffer = readbuffer + (s.recv(1024)).decode("utf-8")
		temp = readbuffer.split("\n")
		readbuffer = temp.pop()

		for line in temp: 
			print(line)
			Loading = loadingComplete(line)
	sendMessage(s, "joined chat")

def loadingComplete(line): 
	if("End of /NAMES list" in line): 
		return False 
	else: 
		return True

def timeout(s, user, time = 60):
	sendMessage(s, "/timeout " + user + " " + str(time)) 

def ban(s, user):
	sendMessage(s, "/ban " + user)

def unban(s, user):
	sendMessage(s, "/unban " + user)

def followers_only(s, length: str):
	'''changes the chat to follower mode, must come in form: 
	30m, 1h, 1d, 1w, or 3mo'''
	sendMessage(s, "/followers " + length)

def followers_off(s): 
	sendMessage(s, "/followersoff")

def slowmode(s, time = 60): 
	sendMessage(s, "/slow " + str(time))

def slow_off(s): 
	sendMessage(s, "/slowoff")

def emote_only(s): 
	sendMessage(s, "/emoteonly")

def emote_off(s): 
	sendMessage(s, "/emoteonlyoff")


s = openSocket()
joinRoom(s)
readbuffer = ""

comm = re.compile('^!\w+\s\S+')
comm2 = re.compile('^!\S+\s')


while True: 
	readbuffer = readbuffer + (s.recv(1024)).decode("utf-8")
	temp = readbuffer.split("\n")
	readbuffer = temp.pop()

	for line in temp: 
		print(line)
		if "PING :tmi.twitch.tv" in line: 
			encoded_send(s, "PONG :tmi.twitch.tv\r\n")
			print("Pong sent")
			break

		user = getUser(line)
		message = getMessage(line)
		print(user + " :" + message)	
		
		
		if "testing123" in message: 
			sendMessage(s, "Test done")
			sendMessage(s, "/w " + user + " Test received")
			timeout(s, user, time = 5)
			break

		if "slowon" in message: 
			sendMessage(s, "putting it on slowmode")
			slowmode(s)
			break

		if "slowoff" in message: 
			sendMessage(s, "slowmode is turninig off")
			slow_off(s)
			break

		if "followerson" in message: 
			sendMessage(s, "putting in in followers only")
			followers_only(s, "30m")
			break

		if "followersoff" in message:
			sendMessage(s, "turning off followers only")
			followers_off(s)
			break 
		

		
		m = re.match('^!\w+', message)
		#m = re.match('^!\S+\s\S+', message)
		if m: 
			print('Match found', m.group())
			print(re.sub(r'!', "", message))
			read_command(re.sub(r'!', "", message))
			break 
		else: 
			print("no match")
			break
				

		'''
		if "!up" in message: 
			moveMouse(30, "UP")
			sendMessage(s, "moved mouse up")
			break

		if "!down" in message: 
			moveMouse(30, "DOWN")
			sendMessage(s, "moved mouse down")
			break

		if "!left" in message: 
			moveMouse(30, "LEFT")
			sendMessage(s, "moved mouse left")
			break

		if "!right" in message: 
			moveMouse(30, "RIGHT")
			sendMessage(s, "moved mouse right")
			break
		'''



