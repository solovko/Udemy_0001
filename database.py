import pymongo
from pymongo.database import Database



class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None  ## static property>> all dB created wil have same URI

    # Normaly we will initialise in __init_ method
    # It would allow to create different DB witth different  URL but this is not what we
    # def __init__(self):
    # self.url = ""
    # self.database = Name
    @staticmethod
    def insert(collection: object, data: object) -> object:
        """

        :rtype: object
        """
        Database.DATABASE[collection].insert(data)

    # Collection and data are from post.py

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: object, query: object) -> object:
        pass
        # want there. In this project we want unique data base we do not need init method
        return Database.DATABASE[collection].find_one(query)

    # method belong only to Database class and NOT to its instances
    def initialize() -> object:
        client = pymongo.MongoClient(Database.URI)  # URI is a part of class Database
        # so we use through dot operator
        Database.DATABASE = client['fullstack']  # contains now database created for this project
