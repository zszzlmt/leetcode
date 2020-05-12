class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        uppers = sum([True if c.isupper() else False for c in word])
        if not uppers or uppers == len(word):
            return True
        elif uppers == 1 and word[0].isupper():
            return True
        else:
            return False
