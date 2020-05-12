class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        from collections import Counter

        counter = Counter(arr1)
        result = list()
        for num in arr2:
            if num in counter:
                result += [num for _ in range(counter[num])]
        all_keys = set(list(counter.keys()))
        sort_keys = set(arr2)
        other_keys_asc = sorted(list(all_keys-sort_keys))
        for num in other_keys_asc:
            result += [num for _ in range(counter[num])]

        return result

