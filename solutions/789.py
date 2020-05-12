class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        best_ghost = min([abs(ghosts[idx][0] - target[0]) + abs(ghosts[idx][1] - target[1]) for idx in range(len(ghosts))])
        player = abs(target[0]) + abs(target[1])
        return True if player < best_ghost else False
