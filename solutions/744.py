class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        base = ord('a')
        tar = ord(target)
        offset = 1
        while True:
            c = chr(((tar + offset) - base) % 26 + base)
            if c in letters:
                return c
            offset += 1
