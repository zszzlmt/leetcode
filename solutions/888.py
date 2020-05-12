class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        from collections import Counter

        ca = Counter(A.split(" "))
        cb = Counter(B.split(" "))
        res = list()

        for key, value in ca.items():
            if value == 1 and key not in cb:
                res.append(key)
        for key, value in cb.items():
            if value == 1 and key not in ca:
                res.append(key)

        return res