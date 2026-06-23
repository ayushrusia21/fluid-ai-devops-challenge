from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

mongo_host = os.getenv("MONGO_HOST", "mongodb")

@app.route("/")
def home():
    try:
        client = MongoClient(f"mongodb://{mongo_host}:27017/")
        client.admin.command("ping")
        return "Fluid AI DevOps Assessment - DB Connected"
    except Exception as e:
        return f"Database Connection Failed: {str(e)}", 500

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
