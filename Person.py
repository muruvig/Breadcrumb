class Person:
	def __init__(self, MacAddress, visits):
		self.MacAddress = MacAddress
		self.visits = []

	def getID(self):
		return self.MacAddress

	def getVisits(self):
		for(visit in self.visits):
			print(visit.getInfo())

	def append(visit):
		self.visits.append(visit)
	