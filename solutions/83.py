# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        res = None
        p = head
        while p != None:
            if pre != p.val:
                pre = p.val
                if res == None:
                    res = ListNode(pre)
                    pr = res
                else:
                    pr.next = ListNode(pre)
                    pr = pr.next
            p = p.next
        return res