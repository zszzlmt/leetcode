class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        set_t = set(T)
        res = str()
        for i in S:
            if i in set_t:
                set_t.remove(i)
                res += i
        return res + ''.join(list(set_t))
# from collections import defaultdict
#
# class Solution:
#     def customSortString(self, S, T):
#         if not S:
#             return T
#         d = defaultdict(int)
#         not_S = list()
#         for idx in range(len(T)):
#             d[T[idx]] += 1
#             if T[idx] not in S:
#                 not_S.append((idx, T[idx]))
#         res = list()
#         for item in S:
#             if item in d:
#                 for times in range(d[item]):
#                     res.append(item)
#         for item in not_S:
#             res.insert(item[0], item[-1])
#         return ''.join(res)
#
if __name__ == '__main__':
    a = Solution()
    s = input()
    t = input()
    print (a.customSortString(s, t))