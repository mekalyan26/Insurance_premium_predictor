# DB Connections
# importing mongodb file
import ssl
import pymongo
import json
import pandas as pd
import sys
from exception_handling.exception_handling import InsuranceException as MongoDbException


class MongoDBOperation:
    def __init__(self, user_name=None, password=None):
        try:
            if user_name is None or password is None:
                # creating initial object to fetch mongodb credentials
                credentials = {
                    "user_name": "username",
                    "password": "password"
                }  # get_mongo_db_credentials()  # return dictionary with user name and password
                self.__user_name = credentials['user_name']
                self.__password = credentials['password']
            else:
                self.__user_name = user_name
                self.__password = password

        except Exception as e:
            mongo_db_exception = MongoDbException(
                "Failed to instantiate mongo_db_object in module [{0}] class [{1}] method [{2}]"
                    .format(MongoDBOperation.__module__.__str__(), MongoDBOperation.__name__,
                            "__init__"))
            raise Exception(mongo_db_exception.error_message_detail(str(e), sys)) from e
