#!/usr/bin/env python3
"""
lists all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """
    This function lists all doc in a collection
    Return an empty list if no document in the collection
    """
    if not mongo_collection:
        return []
    documents = mongo_collection.find()
    return [post for post in documents]
