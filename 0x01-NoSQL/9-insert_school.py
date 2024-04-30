#!/usr/bin/env python3
"""
This module insert a document in Python
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs
    """
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
