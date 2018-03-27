from collections import defaultdict


class Solution(object):

    valid = None

    def __traval__(self, l):
        for word in d[l]:
            for next in d[l + 1]:
                if next[:-1] == word:
                    self.valid.add(next)
                    self.__traval__(next, l + 1)

    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        d = defaultdict(list)
        valid = set()
        for word in words:
            d[len(word)].append(word)
        for word in d[1]:
            self.valid.add(word)
            self.__traval__(1)
        valid = list(self.valid)
        max_len = max([len(word) for word in valid])
        res = list()
        for word in valid:
            if len(word) == max_len:
                res.append(word)
        res.sort()
        return res[0]
