from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD opeartions for the 'Animal' collection in MongoDB """

    def __init__(self, username, password):
        # connect to our local instance of MongoDB using the credentials provided,
        # and store the client object for future use
        # self.client = MongoClient('localhost:47878', username=username, password=password, authSource='AAC')
        self.client = MongoClient('mongodb://%s:%s@localhost:47878' % (username, password))
        
        # Get a reference to the 'AAC' database within MongoDB using the client above
        # This will be used to perform our CRUD operations
        self.database = self.client['AAC']
        
        self.connected = True
        
    def is_connected(self):
        return self.connected

    def create(self, data):
        # Return 'False' if we don't have any data to insert
        if data is None:
            return False
        
        try:
            # insert a single document into the animals collection
            insertRet = self.database.animals.insert_one(data)
            return insertRet.acknowledged
        except:
            raise Exception("Error creating new record")
        
        return False

    def read(self, data):
        # Default to an empty object (query all documents) if no query
        # data is given
        if (data is None):
            data = {}
            
        try:
            # Query the results using the data provided and return the data
            # from MongoDB in a python list
            results = self.database.animals.find(data, {"_id":False})
            return list(results)
        except:
            raise Exception("Error reading data")

    def update(self, query, criteria):
        # Default to an empty object (query all documents) if no query
        # data is given
        if (query is None):
            query = {}
        if (criteria is None):
            criteria = {}
            
        try:
            # Query the results using the data provided and return the data
            # from MongoDB in a python list
            results = self.database.animals.update_many(query, {"$set": criteria})
            return { "acknowledged": results.acknowledged, "matchedCount": results.matched_count, "modifiedCount": results.modified_count }
        except:
            raise Exception("Error updating data")
            
    def delete(self, query):
        if (query is None):
            raise Exception("Use an empty dict to delete all records, or a valid dict to delete some records.")
            
        try:
            results = self.database.animals.delete_many(query)
            return { "acknowledged" : results.acknowledged, "deletedCount" : results.deleted_count }
        except:
            raise Exception("Error deleting data")
            