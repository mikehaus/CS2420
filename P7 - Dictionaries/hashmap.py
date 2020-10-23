"""
HashMap ADT P7 CS2420
Mike Hollingshaus
"""

#-------- START HASHMAP CLASS DECLARATION --------#

class HashMap():

    def __init__(self):
        """
        HashMap Class Constructor
        """
        self._capacity = 8
        self._size = 0
        self._keys = []
        self.dictionary = [None] * 8

    def hash(self, key):
        """
        Get index of our array for
        specific string key
        """
        length = len(self.dictionary)
        return hash(key) % length

    def get(self, key, default=None):
        """
        Return the value for key if key is in the dictionary,
        else default. If default is not given, it defaults to none.
        """
        index = self.hash(key)
        if self.dictionary[index] is None:
            return default
        for i in range(index, len(self.dictionary)):
            keyValuePair = self.dictionary[i]
            if keyValuePair[0] == key:
                return keyValuePair[1]
        return default

    def set(self, key, value):
        """
        Add the key, value pair to the hashMap. After adding,
        if load factor is >=80%, rehash the map into a map
        double its current capacity.
        """
        index = self.hash(key)
        if self.dictionary[index] is not None:
            # If index is already filled at index (collision)
            if self.dictionary[index][0] != key:
                for i in self.dictionary:
                    if i[0] is None:
                        self.dictionary[i] = [key, value]
                        self._size += 1
                        self.keys.append([key, value])
            # If filled and matches key
            else:
                for keyValuePair in self.dictionary:
                    if keyValuePair[0] == key: 
                        self.dictionary[index] = [key, value]
                        break
                    if keyValuePair is None:
                        self.dictionary[index] = [key, value]
                        self._size += 1
                        self.keys.append([key, value])
                        break
        # if index is empty
        else:
            self.dictionary[index] = [key, value]
            self.size += 1
            self.keys.append([key, value])
        # Check load balance
        if self.isLoadBalanceGreaterThan80():
            self.rehash()

    def isLoadBalanceGreaterThan80(self):
        """
        Checks current load balance of hashMap.
        If >=80% returns true. Else returns false.
        """
        loadBalance = self._size / self._capacity
        if loadBalance >= .8:
            return True
        return False

    def clear(self):
        """
        Empty the hashMap
        """
        self._capacity = 8
        self._keys = []
        self._size = 0
        self.dictionary = [None] * 8

    def size(self):
        """
        Returns the size of the map
        """
        return self._size

    def keys(self):
        """
        Returns a list of keys
        """
        return self._keys

    def rehash(self):
        """
        Rebuild the table to reduce the load Factor.
        The new table should be twice the capacity of the
        current table.
        """
        self.clear
        self._capacity = 16
        self.dictionary = [None] * 16
        for keyValuePair in self.keys:
            self.set(keyValuePair[0], keyValuePair[1])
        
#--------- END HASHMAP CLASS DECLARATION -----------#
