class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        sorted_list = sorted(A)
        idx = 0
        result = 0
        k = K
        closest_to_zero = -min([abs(i) for i in sorted_list])
        while k != 0 and idx < len(sorted_list):
            if sorted_list[idx] <= 0:
                result += -sorted_list[idx]
                k -= 1
            else:
                result += sorted_list[idx]
            idx += 1
        if idx < len(sorted_list):
            result += sum(sorted_list[idx:])
        elif k % 2 != 0:
            result += 2 * closest_to_zero
        return result
