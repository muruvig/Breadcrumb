from Ping import *

class Visit:

	if MacID in database:
		def __init__(self, entryTime, location):
			self.entryTime = entryTime
			self.exitTime = None
			self.location = [getLocation()]


	def updateTimeandLocation(self):
		if(not MacID):
			self.exitTime = getPingTime()
			#return the values of exitTime and location array to the database
			self = None
		else:
			self.location.append(getLocation())