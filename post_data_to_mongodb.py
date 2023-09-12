import os
import pymongo
from dotenv import load_dotenv

load_dotenv()
CONNECTION_STRING = os.environ.get("COSMOS_CONNECTION_STRING")

DATA = {
    "id": "101",
    "name": "Intersteller",
    "director": "Christopher Nolan",
    "sale": False
}

def post_data_to_mongodb(db_name, collection_name, connection_string, json_data):
    """Upsert data in MongoDB collection."""
    try:
        # Establish a connection to MongoDB
        client = pymongo.MongoClient(connection_string)
        db = client[db_name]
        collection = db[collection_name]

        # Use "id" as the query filter
        query_filter = {"id": json_data["id"]}

        # Use "$set" to update existing fields or insert a new document if not found
        result = collection.update_one(query_filter, {"$set": json_data}, upsert=True)

        return "Upserted document with _id {}".format(result.upserted_id)
    except Exception as e:
        raise Exception(f"Failed to upsert movie data: {e}")
    finally:
        # Close the MongoDB client connection when done
        client.close()



print(post_data_to_mongodb(
    db_name='imdb',
    collection_name='movies',
    json_data=DATA,
    connection_string=CONNECTION_STRING
))

