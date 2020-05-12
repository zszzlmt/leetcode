from collections import Counter

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        valid = A[0]
        for idx in range(1, len(A)):
            valid_this_time = str()
            string_this_time = Counter(A[idx])
            for c in valid:
                if string_this_time[c] > 0:
                    string_this_time[c] -= 1
                    valid_this_time += c
            valid = valid_this_time
        return list(valid)
