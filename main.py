import os
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
app = Flask(__name__)

client = MongoClient(
    "localhost",
    int(os.getenv("MONGODB_PORT", 27017)),
    username=os.getenv("MONGODB_USER", "root"),
    password=os.getenv("MONGODB_PASSWORD", "root"),
)


@app.route("/")
def hello_world():
    return "Hola Maxi y Gustavo!"
