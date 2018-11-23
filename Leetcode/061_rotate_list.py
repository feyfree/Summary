# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head:
            dummy = ListNode(None)
            dummy.next = head
            p = dummy
            n = 0
            while p.next:
                n += 1
                p = p.next
            k = n- k % n  #求真实移动量
            p.next = dummy.next #将尾结点指向头结点，形成环形
            p = dummy.next
            for i in range(1, k):
                p = p.next
            head = p.next
            p.next = None
            return head
        else:
            return
