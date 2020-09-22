"""
Item class definition.
Basically a node for this
Stack instance.
CS2420 Mike Hollingshaus
"""

########## -- BEGIN ITEM CLASS DEFINITION -- ##########

class Item():
    """
    Class definition of Item (Node).
    """

    def __init__(self, data):
        """
        Item class constructor.
        """
        self._data = data
        self._next = None

    def data(self):
        """
        Return data at Item.
        """
        return self._data

    def next(self):
        """
        Return next item.
        """
        return self._next

########## -- END ITEM CLASS DEFINITION -- ##########
