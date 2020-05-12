class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        from collections import Counter
        import string
        letters = str()
        licensePlate = licensePlate.lower()
        for idx in range(len(licensePlate)):
            if licensePlate[idx] in string.ascii_letters:
                letters += licensePlate[idx]
        count = Counter(letters)

        res = list()
        for w in words:
            count_w = Counter(w)
            for key, cnt in count.items():
                if count_w[key] < cnt:
                    break
            else:
                res.append(w)

        min_length = min([len(res[idx]) for idx in range(len(res))])
        for w in res:
            if len(w) == min_length:
                return w
