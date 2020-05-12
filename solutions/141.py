# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            turtle = head
            hare = head.next
            while turtle and hare:
                if turtle == hare:
                    return True
                turtle = turtle.next
                hare = hare.next.next
            return False
        except:
            return False
