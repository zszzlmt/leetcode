class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl = list(s)
        l = len(sl)
        h = -1
        t = l
        table = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        if l == 0:
            return s
        while True:
            h += 1
            t -= 1
            while sl[h] not in table:
                h += 1
                if h > l - 1:
                    break
            while sl[t] not in table:
                t -= 1
                if t < 0:
                    break
            if h >= t:
                break
            else:
                tmp = sl[h]
                sl[h] = sl[t]
                sl[t] = tmp
        return ''.join(sl)
