class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        pos = 0
        while True:
            if pos == len(bits):
                return False
            if pos == len(bits) - 1:
                return True
            if bits[pos] == 1:
                pos += 2
            else:
                pos += 1
