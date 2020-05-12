class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        base = ord('a')
        lines = 1
        remain = 100
        last = 0
        for item in S:
            need = widths[ord(item) - base]
            if need <= remain:
                remain -= need
                last = 100 - remain
            else:
                lines += 1
                remain = 100 - need
                last = 100 - remain
        return [lines, last]
