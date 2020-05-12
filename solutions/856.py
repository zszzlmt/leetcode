class Solution:

    def __calculate__(self, s):
        if not len(s):
            return 0

        cnt = 0
        base = 0
        parts = list()
        for idx in range(len(s)):
            if s[idx] == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                parts.append(s[base:idx + 1])
                base = idx + 1

        res = 0
        for part in parts:
            if part[1] == ')':  # at least length 2
                res += 1 + self.__calculate__(part[2:])
            else:
                res += 2 * self.__calculate__(part[1:-1])
        return res

    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        return self.__calculate__(S)
