# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        faster = head
        while faster is not None and faster.next is not None:
            faster = faster.next.next
            head = head.next
        return head