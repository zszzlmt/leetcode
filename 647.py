class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum([s[i:j] == s[i:j][::-1]  for j in range(len(s) + 1) for i in range(j)])
