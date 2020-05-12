# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import defaultdict


class Solution(object):
    values = None

    def __traval__(self, n):
        tmp = n.val
        if n.left:
            tmp += self.__traval__(n.left)
        if n.right:
            tmp += self.__traval__(n.right)
        self.values.append(tmp)
        return tmp

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        self.values = list()
        self.__traval__(root)
        d = defaultdict(int)
        max_fre = 0
        res = list()
        for i in self.values:
            d[i] += 1
            if d[i] == max_fre:
                res.append(i)
            elif d[i] > max_fre:
                res = list()
                res.append(i)
                max_fre = d[i]
        return res
