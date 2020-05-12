import bisect

class Solution(object):

    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        # d = dict()
        # for idx in range(len(S)):
        #     c = S[idx]
        #     if c not in d:
        #         d[c] = [idx]
        #     else:
        #         d[c].append(idx)
        #
        # l = len(S)
        # res = 0
        # for w in words:
        #     flag = True
        #     idx = 0
        #     for c in w:
        #         if idx == l:
        #             flag = False
        #             break
        #         if c not in d:
        #             flag = False
        #             break
        #         tmp = bisect.bisect_right(d[c][idx:], c)
        #         if tmp == 0:
        #             if idx != 0 or d[c][0] != c:
        #                 flag = False
        #                 break
        #         idx = tmp + 1
        #     if flag:
        #         res += 1
        # return res
        res = 0
        for w in words:
            head = 0
            flag = True
            l = len(S)
            for c in w:
                pos = S.find(c, head)
                if pos == -1:
                    flag = False
                    break
                head = head + 1
            if flag:
                res += 1
        return res