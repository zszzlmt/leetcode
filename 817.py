# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        sg = set(G)
        res = 0
        while head is not None:
            if head.val in sg:
                res += 1
                while head.next is not None and head.next.val in sg:
                    head = head.next
            head = head.next

        return res
