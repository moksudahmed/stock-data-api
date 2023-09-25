import pymongo
from bson.json_util import dumps

def read(collection_name):
    # MongoDB connection information
    mongo_uri = "mongodb+srv://moksud:Sylhet3100@cluster0.2jzvkyv.mongodb.net/?retryWrites=true&w=majority"  # Change to your MongoDB URI if necessary
    db_name = "dse"  # Change to your database name if necessary
   # collection_name = "stocks"  # Change to your collection name if necessary

    # Connect to MongoDB
    client = pymongo.MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    # Query for reading data
    query = {}  # An empty query to match all documents

    # Exclude the '_id' field from the result using the projection parameter
    cursor = collection.find(query, projection={'_id': False})

    # Serialize the result to JSON using bson.json_util.dumps
    result = dumps(cursor)

    # Close the MongoDB client
    client.close()

    return result

