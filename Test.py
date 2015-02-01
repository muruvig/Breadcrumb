from pymongo import *
from Ping import *
from json import *

def main():
	client = MongoClient()
	db = client.sb_hack
	collection =db.testData
	data = ping()
	for e in data:
		add_to_database(e)

def test():
	client = MongoClient()
	db = client.sb_hack
	collection = db.testData
	data = ping()[0]
	# for e in range(10):
	# 	m = e['macAddress']
	# 	minfo = e['mapInfo']
	# 	currtime = e['statistics']['currentServerTime']
	# 	intime = e['statistics']['firstLocatedTime']
	# 	outtime = None
	# 	collection.update({'macAddress':m}, {'$push':{'visit_list':{'mapInfo':minfo, 'pingTime':currtime, 'entryTime':intime, 'exitTime':outtime]}, {'location_list':{'location':minfo, 'pingTime':currtime}}}})
	# collection.update({'name':'bye'},{'$push':{'testing':data[0]['statistics']['firstLocatedTime'], 'none':None}})
	# for e in data:
	collection.update({'macAddress':data['macAddress']}, {'$push':{'visit_list':{'mapInfo':data['mapInfo'], 'pingTime':data['statistics']['currentServerTime'], 'entryTime':data['statistics']['firstLocatedTime'], 'exitTime':data['statistics']['currentServerTime']}, 'location_list':{'location':data['mapInfo'], 'pingTime':data['statistics']['currentServerTime']}, 'checker':'yes'}})
	print(data['macAddress'])
test()