class Solution(object):

    paths = None
    tar = None

    def __traval__(self, graph, node, path):
        if node == self.tar:
            self.paths.append(path)
            return
        for next_node in graph[node]:
            self.__traval__(graph, next_node, path + [next_node])

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.paths = list()
        self.tar = len(graph) - 1
        self.__traval__(graph, 0, [0])
        return self.paths
