#!/usr/bin/python3
"""
This module defines the lookup function that returns the list
of available attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        List of strings representing the attributes and methods of the object.
    """
    return dir(obj)

