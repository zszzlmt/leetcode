# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        if head is None:
            return 0
        digits = list()
        while head is not None:
            digits.append(head.val)
            head = head.next
        result = 0
        base = 1
        for digit in digits[::-1]:
            result += digit * base
            base *= 2
        return result