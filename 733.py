class Solution(object):
    
    img = None
    col = None
    row = None
    c = None
    traval = None
    
    def __flood__(self, x, y, tar):
        if self.img[x][y] == tar:
            self.img[x][y] = self.c
            self.traval[x][y] = 1
            print x, y, self.img
            if self.__check__(x - 1, y) and not self.traval[x - 1][y]:
                self.__flood__(x - 1, y, tar)
            if self.__check__(x + 1, y) and not self.traval[x + 1][y]:
                self.__flood__(x + 1, y, tar)
            if self.__check__(x, y - 1) and not self.traval[x][y - 1]:
                self.__flood__(x, y - 1, tar)
            if self.__check__(x, y + 1) and not self.traval[x][y + 1]:
                self.__flood__(x, y + 1, tar)
        else:
            return
        
    def __check__(self, x, y):
        if x < 0 or x >= self.row:
            return False
        if y < 0 or y >= self.col:
            return False
        return True
    
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if len(image) == 0:
            return image
        self.img = image
        self.col = len(image[0])
        self.row = len(image)
        self.c = newColor
        self.traval = list()
        for row in range(self.row):
            tmp = [0] * self.col
            self.traval.append(tmp)
        
        self.__flood__(sr, sc, image[sr][sc])
        return self.img
        