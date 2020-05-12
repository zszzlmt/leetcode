# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    paths = list()

    def __traval__(self, node, path):
        if node is None:
            return
        if node.left is None and node.right is None:
            self.paths.append(path + [node.val])
            return
        if node.left:
            self.__traval__(node.left, path + [node.val])
        if node.right:
            self.__traval__(node.right, path + [node.val])
        return

    def __find_node__(self, node, val):
        if node is None:
            return False
        if node.val == val:
            return node
        if node.left:
            left = self.__find_node__(node.left, val)
            if left:
                return left
        if node.right:
            right = self.__find_node__(node.right, val)
            if right:
                return right
        return False

    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.paths = list()
        self.__traval__(root, [])
        max_depth = max([len(path) for path in self.paths])
        deepest = list()
        one_deepest_path = None
        for path in self.paths:
            if len(path) == max_depth:
                one_deepest_path = path
                deepest.append(set(path))
        common = list()
        for idx in range(1, len(deepest)):
            tmp = list()
            for element in deepest[0] & deepest[idx]:
                tmp.append(element)
            common.append(tmp)
        if not len(common):
            common = set(deepest[0])
        else:
            tmp = set(common[0])
            for idx in range(1, len(common)):
                tmp = tmp & set(common[idx])
            common = tmp
        sub_root_val = one_deepest_path[max([one_deepest_path.index(element) for element in common])]
        return self.__find_node__(root, sub_root_val)