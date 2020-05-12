from collections import defaultdict


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row_0 = defaultdict(int)
        row_1 = defaultdict(int)
        row_2 = defaultdict(int)

        for i in ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']:
            row_0[i] = 0
        for i in ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']:
            row_1[i] = 1
        for i in ['z', 'x', 'c', 'v', 'b', 'n', 'm']:
            row_2[i] = 2

        res = list()
        for w in words:
            flag = True
            row_d = None
            for c in w:
                c = c.lower()
                if row_d is None:
                    if c in row_0:
                        row_d = row_0
                    elif c in row_1:
                        row_d = row_1
                    elif c in row_2:
                        row_d = row_2
                    continue
                else:
                    if c not in row_d:
                        flag = False
                        break
            if flag:
                res.append(w)
        return res
