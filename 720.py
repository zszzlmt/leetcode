from collections import defaultdict


class Solution(object):

    valid = None

    def __traval__(self, word, l, d):
        self.valid.add(word)
        for next in d[l + 1]:
            if next[:-1] == word:
                self.__traval__(next, l + 1, d)

    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        d = defaultdict(list)
        self.valid = set()
        for word in words:
            d[len(word)].append(word)
        for word in d[1]:
            self.__traval__(word, 1, d)
        valid = list(self.valid)
        max_len = max([len(word) for word in valid])
        res = list()
        for word in valid:
            if len(word) == max_len:
                res.append(word)
        res.sort()
        return res[0]
