from collections import defaultdict
import bisect


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        d = defaultdict(list)
        res = list()
        values = set(temperatures)
        solved = dict()
        for idx in range(len(temperatures)):
            d[temperatures[idx]].append(idx)
        for idx in range(len(temperatures) - 1):
            item = temperatures[idx]
            min_pos = None
            if item in solved:
                if solved[item] == -1:
                    res.append(0)
                    continue
                elif idx < solved[item]:
                    res.append(solved[item] - idx)
                    continue
            next_pos = None
            for next_value in values:
                if next_value > item and d[next_value][-1] > idx:
                    tmp = d[next_value][bisect.bisect_right(d[next_value], idx)]
                    pos = tmp - idx
                    if not min_pos or pos < min_pos:
                        min_pos = pos
                        next_pos = tmp
            if not min_pos:
                res.append(0)
                solved[item] = -1
            else:
                res.append(min_pos)
                solved[item] = next_pos
        return res + [0]

        # res = list()
        # for idx in range(len(temperatures) - 1):
        #     item = temperatures[idx]
        #     flag = False
        #     for idx_next in range(idx + 1, len(temperatures)):
        #         if temperatures[idx_next] > item:
        #             res.append(idx_next - idx)
        #             flag = True
        #             break
        #     if not flag:
        #         res.append(0)
        # res.append(0)
        # return res

        # res = list()
        # for idx in range(len(temperatures) - 1):
        #     try:
        #         res.append(1 + [tem > temperatures[idx] for tem in temperatures[idx + 1:]].index(True))
        #     except ValueError as v:
        #         res.append(0)
        # res.append(0)
        # return res