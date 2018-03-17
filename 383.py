class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag = list(magazine)
        for c in ransomNote:
            try:
                idx = mag.index(c)
            except ValueError as v:
                return False
            else:
                del mag[idx]
        return True