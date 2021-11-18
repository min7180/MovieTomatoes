# MongoDB Access and CRUD test
from pymongo import MongoClient

# 1. MongoDB Connection
client = MongoClient('localhost', 27017)  # (IP address, Port number)
db = client['local']  # Allocating 'local' DB
collection = db.get_collection('test')  # Allocating 'review' Collection

# MongoDB > database > collection > document

# 'localhost' == 127.0.0.1 == 192.168.0.5
cilent = MongoClient('localhost', 27017)
db = client['local']
collection = db.get_collection('test')

data = {'name': 'cherry', 'age': 8}
collection.insert_one(data)

