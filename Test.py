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

def add_to_database(device):
	return None

def test():
	client = MongoClient()
	db = client.sb_hack
	collection = db.testData
	data = ping()
	collection.insert(data)

test()