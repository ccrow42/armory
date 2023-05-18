from flask import Flask
import pymongo
import urllib.parse
import os

#username = urllib.parse.quote_plus('porxie')
#password = urllib.parse.quote_plus('porxie')

username = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PASS')
server = os.getenv('MONGO_NODE')

app = Flask(__name__)


def get_document_count(database_name, collection_name):
    # Create a connection to the MongoDB instance running on localhost
    client = pymongo.MongoClient("mongodb://%s:%s@%s:27017/" % (username, password, server)) 

    # Access the specific database
    db = client[database_name]

    # Access the specific collection
    collection = db[collection_name]

    # Use the count_documents() method to get the number of documents
    document_count = collection.count_documents({})

    return document_count

# Use the function
docCount = get_document_count("porxbbq", "orders")


@app.route('/')
def hello_geek():
    return ("%s orders served from PorxBBQ" % docCount)

print ("%s orders served from PorxBBQ" % docCount)
app.run(host='0.0.0.0')

