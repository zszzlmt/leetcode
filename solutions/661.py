class Solution(object):

    def __check__(self, x, y, row, col):
        if 0 <= x < row and 0 <= y < col:
            return True
        return False

    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(M)
        col = len(M[0])
        res = list()

        for x in range(row):
            tmp = list()
            for y in range(col):
                base_x = x - 1
                base_y = y - 1
                value = 0
                cnt = 0
                for con_x in range(3):
                    for con_y in range(3):
                        if self.__check__(base_x + con_x, base_y + con_y, row, col):
                            value += M[base_x + con_x][base_y + con_y]
                            cnt += 1
                new_val = value / cnt
                tmp.append(new_val)
            res.append(tmp)
        return res