class Solution(object):

    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        d = dict()
        for idx in range(len(S)):
            c = S[idx]
            if c not in d:
                d[c] = [idx]
            else:
                d[c].append(idx)


        # res = 0
        # for w in words:
        #     flag = True
        #     l = len(S)
        #     for c in w:
        #         if head == l:
        #             flag = False
        #             break
        #         pos = S[head:].find(c)
        #         if pos == -1:
        #             flag = False
        #             break
        #         head = pos + head + 1
        #     if flag:
        #         res += 1
        # return res