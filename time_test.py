import time
import threading

# start_time = time.time()
# while(True):
# 	endtime = time.time()
# 	print(endtime-start_time)


class timeThread(threading.Thread):
	# def start(self):
	# 	self.start = time.time()
	# 	self.current = time.time()
	# 	self.run = True

	def run(self):
		self.start = time.time()
		while(True):
			self.current = time.time()
			print(self.current-self.start)

#class actionThread(threading.Thread):


if __name__ == "__main__": 
	a = timeThread()
	a.start()
