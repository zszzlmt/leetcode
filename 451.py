class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not len(s):
            return ''
        from collections import Counter
        count = Counter(s)
        count = count.most_common()

        res = ''
        for (c, times) in count:
            res += ''.join([c for _ in range(times)])

        return res
