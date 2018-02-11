class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        d = dict()
        l = len(answers)
        if l == 0:
            return 0
        for item in answers:
            if item not in d:
                d[item] = 1
            else:
                d[item] += 1
        res = 0
        for key, value in d.items():
            if key + 1 >= d[key]:
                res += key + 1
            else:
                times = d[key] // (key + 1)
                if d[key] % (key + 1) == 0:
                    res += times * (key + 1)
                else:
                    res += (times + 1) * (key + 1)
        return res