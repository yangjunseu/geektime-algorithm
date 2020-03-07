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
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1

        head = l = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                l.next,l1 = l1,l1.next
                l = l.next
            else:
                l.next,l2 = l2,l2.next
                l = l.next

        while l1:
            l.next,l1 = l1,l1.next
            l = l.next

        while l2:
            l.next,l2 = l2,l2.next
            l = l.next

        return head.next
