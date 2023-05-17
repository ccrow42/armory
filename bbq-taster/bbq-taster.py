from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

@app.route('/')
def hello_geek():
    return (myclient.list_database_names())


if __name__ == "__main__":
    app.run(debug=True)
