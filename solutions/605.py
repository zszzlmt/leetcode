class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        cnt = 0
        if not flowerbed[0] and (len(flowerbed) == 1 or not flowerbed[1]):
            flowerbed[0] = 1
            cnt += 1
        if not flowerbed[-1] and (len(flowerbed) == 1 or not flowerbed[-2]):
            flowerbed[-1] = 1
            cnt += 1
        for idx in range(1, len(flowerbed)):
            if not flowerbed[idx] and not flowerbed[idx - 1] and not flowerbed[idx + 1]:
                flowerbed[idx] = 1
                cnt += 1
        if cnt >= n:
            return True
        return False
