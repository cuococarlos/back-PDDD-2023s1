import os
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
app = Flask(__name__)

client = MongoClient(
    "localhost",
    int(os.getenv("MONGODB_PORT", 27017)),
    username="root",
    password="123456",
)


@app.route("/")
def hello_world():
    return "Hola Maxi y Gustavo!"
