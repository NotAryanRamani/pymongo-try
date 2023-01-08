from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/PyMongoTry'
mongo = PyMongo(app)

from flask_app import routes