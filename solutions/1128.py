class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        from collections import defaultdict
        cluster_to_values = defaultdict(set)
        cluster_to_idxs = defaultdict(list)
        for idx in range(len(dominoes)):
            i, j = dominoes[idx]
            for idxx in cluster_to_values:
                if (i, j) in cluster_to_values[idxx]:
                    cluster_to_idxs[idxx].append(idx)
                    break
            else:
                idxx = len(cluster_to_idxs)
                cluster_to_idxs[idxx].append(idx)
                cluster_to_values[idxx].add((i, j))
                cluster_to_values[idxx].add((j, i))
        result = 0
        for idx_list in cluster_to_idxs.values():
            result += (len(idx_list) - 1) * (len(idx_list)) / 2
            result = int(result)
        return result