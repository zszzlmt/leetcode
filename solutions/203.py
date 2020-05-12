# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        p = head.next
        pp = head
        while p:
            if p.val == val:
                pp.next = p.next
                p = p.next
            else:
                p = p.next
                pp = pp.next
        return head
