class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        if l == 0:
            return True
        stack = []
        right = [')', ']', '}']
        other = {')':'(', ']':'[', '}':'{'}
        for idx in range(l):
            c = s[idx]
            if c in right:
                if len(stack) > 0:
                    if stack[-1] == other[c]:
                        del stack[-1]
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(c)
        if len(stack) != 0:
            return False
        return True