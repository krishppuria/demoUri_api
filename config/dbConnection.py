import pymongo
import os

url = os.environ.get('mongo_uri')

print('url',url)
client = pymongo.MongoClient(url)

db = client['demoUri']
