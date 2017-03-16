import pymongo
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')
db = client.test_database
collection = db.test_collection
import datetime
post = {"author": "Mike",
     "text": "My first blog post!",
     "tags": ["mongodb", "python", "pymongo"],
     "date": datetime.datetime.utcnow()}
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print post_id
