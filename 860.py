class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        cnt_5 = 0
        cnt_10 = 0
        for val in bills:
            if val == 5:
                cnt_5 += 1
            elif val == 10:
                cnt_5 -= 1
                cnt_10 += 1
            else:
                if cnt_10 >= 1:
                    cnt_10 -= 1
                    cnt_5 -= 1
                else:
                    cnt_5 -= 3
            if cnt_5 < 0 or cnt_10 < 0:
                return False
        return True