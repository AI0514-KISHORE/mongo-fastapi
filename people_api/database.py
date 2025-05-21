"""DATABASE
MongoDB database initialization
"""

# # Installed # #
from pymongo import MongoClient
from pymongo.collection import Collection

# # Package # #
from .settings import mongo_settings as settings

__all__ = ("client", "collection")

connection_string = "mongodb://root:FQ854rewt2Y0YC@89.218.54.78:2767/?authMechanism=DEFAULT&authSource=admin"

client = MongoClient(settings.uri)
collection: Collection = client[settings.database][settings.collection]
