from config.dbConnection import db
from django.db import models
from datetime import datetime, timedelta
import boto3
from django.conf import settings
from bson import ObjectId
from django.db.models import Q

# --------------------------------------------------------------
# Account model
# --------------------------------------------------------------

class Account(models.Model):
    collection_name = 'users'

    # ------------------------------------------------
    # Create a new account
    # ------------------------------------------------
    
    @classmethod
    def create(cls, data):
        result = db[cls.collection_name].insert_one(data)
        return db[cls.collection_name].find_one({'_id': result.inserted_id},{'password':0})
    
    # ---------------------------------------------------------------
    # Get user by email
    # ---------------------------------------------------------------
    
    @classmethod
    def get(cls, email):
        return db[cls.collection_name].find_one({'email': email,"account": {'$ne': 'Inactive'}},{'_id': 0, 'password':0})
   
    # ---------------------------------------------------------------
    # Get user by email
    # ---------------------------------------------------------------
    
    @classmethod
    def getUserByEmail(cls, email):
        return db[cls.collection_name].find_one({'email': email})
    
    # ---------------------------------------------------------------
    # Sign in - Acount
    # ---------------------------------------------------------------
    
    @classmethod
    def signIn(cls, email):
        return db[cls.collection_name].find_one({'email': email})

    

    @classmethod
    def getUserById(cls, id):
        return db[cls.collection_name].find_one({'_id': ObjectId(id)},{'password':0})

    
    # ---------------------------------------------------------------
    # Get user by Phone Number
    # ---------------------------------------------------------------
    
    @classmethod
    def getUserByPhone(cls, phone):
        return db[cls.collection_name].find_one({'phone': phone},{'_id': 0, 'password':0})
