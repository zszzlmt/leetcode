class Solution(object):
    l = '('
    r = ')'
    res = []

    def generate(self, str, c, unuse_l, left_l, left_r):
        if left_l == 0 and left_r == 0:
            self.res.append(str + c)
            return
        if left_l > 0:
            self.generate(str + c, self.l, unuse_l + 1, left_l - 1, left_r)
        if left_r > 0 and unuse_l > 0:
            self.generate(str + c, self.r, unuse_l - 1, left_l, left_r - 1)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return ['']
        if n == 1:
            return ['()']
        self.res = []
        self.generate('', self.l, 1, n - 1, n)
        return self.res
