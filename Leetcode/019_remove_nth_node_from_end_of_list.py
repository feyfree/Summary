# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        p = dummy
        q = dummy
        i = 0
        while i < n:
            i += 1
            p = p.next
        while p.next:
            p = p.next
            q = q.next
        q.next = q.next.next
        return dummy.next