import string
import socket
import re
from gen_functions import*
import chat_bot

def f(x):
    return {
        'a': 1,
        'b': 2,
    }[x]

def f1(x): 
	zed = {
		'a': 1,
		'b': 2,
		'c': 3,
	}[x]
	return zed

def avc1():
	print("1")
	return 1

def avc2():
	print("2")
	return 2

def avc3():
	print("3")
	return 3

def h1(malue):
	jor = {
		'x': avc1(),
		'y': avc2(),
		'z': avc3()
	}[malue]

	return jor

def g1(value, z):
	result = {
		'a': avc1(),#lambda x: x * 5 * z,
  		'b': avc2(),#lambda x: x + 7 + z,
  		'c': avc3()#lambda x: x - 2 - z
	}[value]#(z)

	return result

def one():
    return "January"
 
def two():
    return "February"
 
def three():
    return "March"
 
def four():
    return "April"
 
def five():
    return "May"
 
def six():
    return "June"
 
def seven():
    return "July"
 
def eight():
    return "August"
 
def nine():
    return "September"
 
def ten():
    return "October"
 
def eleven():
    return "November"
 
def twelve():
    return "December"
 
 
def numbers_to_months(argument):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,
        11: eleven,
        12: twelve
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    print(func())

def ptest(orig, *args):
	# for x in args:
	# 	print(x)
	print(args) # this will print all of the arguments

def ptest2(orig, **kwargs):
	# for y in kwargs:
	# 	print(y)
	print(kwargs) #prints dictionary 
	#print(key)

def testprint(input):
	print("hello {} result".format(input))

if __name__ == "__main__": 
	print("aspdok")
	# # print(f('a'))
	# # print(f1('c'))
	# # #print(f1('d'))
	# #print(g1('b', 5))
	# print(g1('a', 3))
	# h1('x')

	#numbers_to_months(6)
	#ptest([1,2,3,4,5,6,7])
	#ptest2([1,2,3,4,5,6,7])
	# ptest(1,2,3,4,5,6,7,8)
	# ptest2(1,two=2,three=3,four=4,five=5,six=6,seven=7,eight=8)

	# john = None 
	# testprint(john)

	if 2 == (1 or 2 or 3 or 4 or 'a'):
		print("True")
	else:
		print("False")