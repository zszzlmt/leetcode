# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        p1 = l1
        p2 = l2
        if p1.val <= p2.val:
            res = ListNode(p1.val)
            p1 = p1.next
        else:
            res = ListNode(p2.val)
            p2 = p2.next
        pr = res
        while p1 != None or p2 != None:
            if p1 != None and p2 != None:
                if p1.val <= p2.val:
                    value = p1.val
                    p1 = p1.next
                else:
                    value = p2.val
                    p2 = p2.next
            elif p1 != None:
                value = p1.val
                p1 = p1.next
            else:
                value = p2.val
                p2 = p2.next
            pr.next = ListNode(value)
            pr = pr.next
        return res
