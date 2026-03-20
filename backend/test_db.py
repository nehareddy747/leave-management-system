from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read MONGO_URI from the environment
mongo_uri = os.getenv("MONGO_URI")

if not mongo_uri:
    print("❌ MONGO_URI is missing from the environment variables.")
    exit(1)

# Hide credentials for safe logging
hidden_uri = mongo_uri.split("@")
safe_uri = "mongodb+srv://***:***@" + hidden_uri[-1] if len(hidden_uri) > 1 else mongo_uri[:30] + "..."

print(f"Connecting with URI: {safe_uri}")

# Initialize MongoClient using ServerApi('1')
client = MongoClient(mongo_uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')
    print("✅ Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("❌ Connection Failed:")
    print(e)