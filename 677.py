class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.d[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        res = 0
        for key, val in self.d.items():
            if key[:len(prefix)] == prefix:
                res += val
        return res

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)