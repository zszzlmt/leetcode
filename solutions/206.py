# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        elif head.next is None:
            return ListNode(head.val)
        res = None
        p = head
        while p is not None:
            pr = ListNode(p.val)
            pr.next = res
            res = pr
            p = p.next
        return res
