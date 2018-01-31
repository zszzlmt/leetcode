class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if len(s) == 0:
            return 0
        dp = [1]
        rec = dict()
        rec[s[0]] = 0
        for idx in range(1, l):
            if not s[idx] in rec:
                rec[s[idx]] = idx
                dp.append(dp[-1] + 1)
            else:
                pos = rec[s[idx]]
                dp.append(idx - pos)
                to_delete = []
                for k, v in rec.items():
                    if v <= pos:
                        to_delete.append(k)
                for k in to_delete:
                    del rec[k]
                rec[s[idx]] = idx
        return max(dp)