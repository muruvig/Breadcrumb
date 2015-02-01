from pymongo import *
from Ping import *
from json import *

def data():
	client = MongoClient()
	db = client.sb_hack
	collection = db.workingData
	x_list = []
	y_list = []
	for element in collection.find().limit(100): #arbitrary limit of 100
		current = element['location_list']
		for location in current:
			x_list.append(location['mapCoordinate']['x'])
			y_list.append(location['mapCoordinate']['y'])
	coords = [x_list, y_list]
	return coords

data()