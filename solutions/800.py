class Solution(object):

    d = {'0': 0,
         '1': 1,
         '2': 2,
         '3': 3,
         '4': 4,
         '5': 5,
         '6': 6,
         '7': 7,
         '8': 8,
         '9': 9,
         'a': 10,
         'b': 11,
         'c': 12,
         'd': 13,
         'e': 14,
         'f': 15}

    def __solve__(self, s):
        if s[0] == s[1]:
            return s[0]
        min_dis = None
        min_res = None
        base = self.d[s[0]] * 16 + self.d[s[1]]
        for c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
            value = self.d[c] * 16 + self.d[c]
            dis = (base - value) ** 2
            if min_dis is None or dis < min_dis:
                min_dis = dis
                min_res = c
        return min_res

    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        res = '#'
        r = color[1:3]
        g = color[3:5]
        b = color[5:7]
        res += (self.__solve__(r)) * 2
        res += (self.__solve__(g)) * 2
        res += (self.__solve__(b)) * 2
        return res