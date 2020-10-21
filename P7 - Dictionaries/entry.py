"""
Entry Class Definition
P7 - Dictionaries CS 2420
Mike Hollingshaus
"""

class Entry(object):
    """
    Dictionary entry class including a key value pair
    """

    def __init__(self, key, value):
        """
        Entry Class Constructor
        """
        self.key = key
        self.value = value