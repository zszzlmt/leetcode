# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        c = 0
        tmp = p1.val + p2.val + c
        c = tmp / 10
        res = ListNode(tmp % 10)
        pr = res
        while True:

            if p1.next == None or p2.next == None:
                if p1.next == None and p2.next == None:
                    if c != 0:
                        pr.next = ListNode(c)
                    break
                elif p1.next == None:
                    tmp = p1
                    p1 = p2
                    p2 = tmp
                p1 = p1.next
                while p1 != None:
                    tmp = p1.val + c
                    c = tmp / 10
                    pr.next = ListNode(tmp % 10)
                    p1 = p1.next
                    pr = pr.next
                if c != 0:
                    pr.next = ListNode(c)
                break

            else:
                p1 = p1.next
                p2 = p2.next
                tmp = p1.val + p2.val + c
                c = tmp / 10
                pr.next = ListNode(tmp % 10)
                pr = pr.next

        return res