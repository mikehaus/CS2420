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
        return hash(key) % self.capacity()

    def capacity(self):
        """
        Returns hashmap capacity
        """
        return self._capacity

    def get(self, key, default=None):
        """
        Return the value for key if key is in the dictionary,
        else default. If default is not given, it defaults to none.
        """
        index = self.hash(key)
        if self.dictionary[index] is None:
            return default
        for i in range(0, self.capacity()):
            keyValuePair = self.dictionary[i]
            if keyValuePair is not None:
                if keyValuePair[0] == key:
                    return keyValuePair[1]
        return default

    def set(self, key, value=None):
        """
        Add the key, value pair to the hashMap. After adding,
        if load factor is >=80%, rehash the map into a map
        double its current capacity.
        """
        index = self.hash(key)
        if self.dictionary[index] is not None:
            # If index is already filled at index (collision)
            if self.dictionary[index][0] != key:
                for i in range(0, len(self.dictionary)):
                    if self.dictionary[i] is None:
                        if value is None:
                            value = 1
                        self.dictionary[i] = [key, value]
                        self._keys.append([key, value])
                        self._size += 1
                        break
                    elif self.dictionary[i][0] == key:
                        if not value:
                            self.dictionary[i][1] += 1
                            break
                        else:
                            self.dictionary[i][1] = value
                            break

            # If filled and matches key
            else:
                if self.dictionary[index][0] == key:
                    if value is None:
                        self.dictionary[index][1] += 1
                    else:
                        self.dictionary[index][1] = value
        # if index is empty
        else:
            if value is None:
                value = 1
            self.dictionary[index] = [key, value]
            self._keys.append([key, value])
            self._size += 1
        # Check load balance
        if self.isLoadBalanceGreaterThan80():
            self.rehash()

    def isLoadBalanceGreaterThan80(self):
        """
        Checks current load balance of hashMap.
        If >=80% returns true. Else returns false.
        """
        loadBalance = self._size / self.capacity()
        if loadBalance >= .8:
            return True
        return False

    def clear(self):
        """
        Empty the hashMap
        """
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
        self._keys = []
        for index in range(0, self.capacity()):
            if self.dictionary[index] is not None:
                indexKey = self.dictionary[index][0]
                valueKey = self.dictionary[index][1]
                keyValuePair = [indexKey, valueKey]
                self._keys.append(keyValuePair)
        self.clear()
        self._capacity = self._capacity * 2
        self.dictionary = [None] * self._capacity
        for keyValuePair in self._keys:
            self.set(keyValuePair[0], keyValuePair[1])
        
#--------- END HASHMAP CLASS DECLARATION -----------#
