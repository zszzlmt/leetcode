# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = head
        s = head
        l = 1
        cnt = 1
        while p.next != None:
            if cnt != n + 1:
                cnt += 1
            else:
                s = s.next
            p = p.next
            l += 1
        if s != head or n != l:
            s.next = s.next.next
        else:
            head = s.next
        return head