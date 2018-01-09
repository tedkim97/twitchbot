import string
import socket
import re

def encoded_send(socket, msg:str):
	socket.send(msg.encode("utf-8"))