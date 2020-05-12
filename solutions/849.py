class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        max_d = 0
        zero_flag = False
        cnt = 0
        for idx in range(len(seats)):
            if seats[idx] == 0:
                if zero_flag:
                    cnt += 1
                else:
                    zero_flag = True
                    cnt = 1
            else:
                zero_flag = False
                if cnt > max_d:
                    max_d = cnt

        max_d =  (max_d + 1) // 2
        if seats[0] == 0:
            max_d = max(max_d, seats.index(1))
        if seats[-1] == 0:
            max_d = max(max_d, seats[::-1].index(1))
        return max_d