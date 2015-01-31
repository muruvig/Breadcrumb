from Ping import *
from Visit import *

class Store:
	openingTime = someHr
	currTime = hr
	closingTime = anotherHr

	def __init__(self):
		self.visits = []

	def append(self, visit):
		self.visits.append(visit)

	def update(self):
		data = ping()
		for visit in data:
			if(not MacID):
				self.exitTime = getPingTime()
				#return the values of exitTime and location array to the database
				self = None
			else:
				self.location.append(getLocation())

	def updateStore(self):
		while currTime <= closingTime:
			currTime += pingTime
			self.update()

print(ping())