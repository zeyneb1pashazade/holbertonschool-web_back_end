#!/usr/bin/env python3
"""
8-all.py
List all documents in a MongoDB collection
"""

def list_all(mongo_collection):
    """
    Returns all documents in a collection
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
