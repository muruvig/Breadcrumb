from pymongo import *
from Ping import *
from json import *

def main():
	client = MongoClient()
	db = client.sb_hack
	collection = db.workingData
	data = ping()
	for element in data:
		if collection.find({'macAddress':element['macAddress']}).count() != 0:
			collection.update({'macAddress':element['macAddress']}, {'$push':{'visit_list':{'mapInfo':element['mapInfo'], 'pingTime':element['statistics']['currentServerTime'], 'entryTime':element['statistics']['firstLocatedTime'], 'exitTime':element['statistics']['currentServerTime']}, 'location_list':{'mapInfo':element['mapInfo'], 'mapCoordinate':element['mapCoordinate'], 'pingTime':element['statistics']['currentServerTime']}}})
		else:
			collection.insert({'macAddress':element['macAddress'], 'visit_list':[{'mapInfo':element['mapInfo'], 'pingTime':element['statistics']['currentServerTime'], 'entryTime':element['statistics']['firstLocatedTime'], 'exitTime':element['statistics']['currentServerTime']}], 'location_list':[{'mapInfo':element['mapInfo'], 'mapCoordinate':element['mapCoordinate'], 'pingTime':element['statistics']['currentServerTime']}]})

main()