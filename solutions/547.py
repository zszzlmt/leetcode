class Solution:

    def traval(self, node):
        if self.travaled[node]:
            return
        self.travaled[node] = True
        for next in range(len(self.M[0])):
            if self.M[node][next] == 1:
                self.traval(next)

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        self.travaled = [False for _ in range(len(M))]
        self.M = M

        res = 0
        for node in range(len(M)):
            if not self.travaled[node]:
                res += 1
                self.traval(node)
        return res
