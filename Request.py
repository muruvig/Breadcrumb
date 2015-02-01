from pymongo import *
from Ping import *
from json import *

def data():
	client = MongoClient()
	db = client.sb_hack
	collection = db.workingData
	coords = [['X', 'Y']]
	for element in collection.find():
		current = element['location_list']
		for location in current:
			coords.append([location['mapCoordinate']['x'], location['mapCoordinate']['y']])
	print(coords)

data()