#!/usr/bin/env python3
"""
11-schools_by_topic.py
Return a list of schools having a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns all school documents containing the given topic in their 'topics' list
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find({ "topics": topic }))
