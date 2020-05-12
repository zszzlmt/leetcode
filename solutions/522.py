class Solution(object):

    def __is_sub__(self, s, bad):
        if len(s) > len(bad):
            return False
        if s == bad:
            return True
        pos = 0
        for idx in range(len(s)):
            tmp = bad[pos:].find(s[idx])
            if tmp == -1:
                return False
            if idx == len(s) - 1:
                return True
            pos += tmp + 1
        return True

    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        str_set = set()
        bad = list()
        for s in strs:
            if s not in str_set:
                str_set.add(s)
            else:
                if s not in bad:
                    bad.append(s)
        strs.sort(key=lambda s: len(s), reverse=True)
        for s in strs:
            if s in bad:
                continue
            flag = True
            for bad_s in bad:
                if self.__is_sub__(s, bad_s):
                    flag = False
                    break
            if flag:
                return len(s)
        return -1


