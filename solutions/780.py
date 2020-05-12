class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        if tx == ty:
            return sx == tx and sy == ty
        while sx != tx or sy != ty:
            if tx < sx or ty < sy:
                return False
            if tx > ty:
                tx -= max([((tx - sx) // ty), 1]) * ty
            else:
                ty -= max([((ty - sy) // tx), 1]) * tx
        return True