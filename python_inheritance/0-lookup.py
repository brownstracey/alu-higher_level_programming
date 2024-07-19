#!/usr/bin/python3
"""
0-lookup.py

This module provides a function to list available attributes
and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj (any): The object to inspect.

    Returns:
        list: A list of attributes and methods of the object.
    """
    return dir(obj)
