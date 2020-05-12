class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:

        def get_sum(A):
            result = 0
            for value in A:
                if abs(value) % 2 == 0:
                    result += value
            return result

        def is_even(num):
            return abs(num) % 2 == 0

        results = list()
        init_sum = get_sum(A)
        results.append(init_sum)

        for value, index in queries:
            previous_value = A[index]
            now_value = A[index] + value
            result_base = results[-1]
            if is_even(previous_value) and is_even(now_value):
                results.append(result_base + value)
            elif is_even(previous_value) and not is_even(now_value):
                results.append(result_base - previous_value)
            elif not is_even(previous_value) and is_even(now_value):
                results.append(result_base + now_value)
            else:
                results.append(result_base)
            A[index] = now_value

        return results[1:]
