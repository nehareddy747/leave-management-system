from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from app.config import Config
import sys

def get_db():
    if not Config.MONGO_URI:
        print("❌ Error: MONGO_URI not found in configuration.")
        sys.exit(1)

    try:
        # Create a new client and connect to the server using ServerApi format
        client = MongoClient(Config.MONGO_URI, server_api=ServerApi('1'))
        
        # Send a ping to confirm a successful connection
        client.admin.command('ping')
        print("✅ Pinged your deployment. You successfully connected to MongoDB!")

        # Retrieve the default database specified in the connection string
        db = client.get_database()
        
        # Fallback if no specific database is set in the URI
        if db.name == 'test' or not db.name:
            db = client['leave_db']
            
        return db
        
    except Exception as e:
        print("❌ Error connecting to MongoDB:")
        print(e)
        # Exiting because the application needs the database to function correctly
        sys.exit(1)

# Initialize the db connection
db = get_db()
