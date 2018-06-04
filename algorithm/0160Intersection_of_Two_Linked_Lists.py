# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        p, q = headA, headB
        a_len, b_len = 0, 0

        while p:
            a_len += 1
            p = p.next

        while q:
            b_len += 1
            q = q.next

        minus = a_len - b_len
        p, q = headA, headB
        if minus > 0:
            while minus:
                p = p.next
                minus -= 1
        else:
            minus = -minus
            while minus:
                q = q.next
                minus -= 1
        while p and q:
            if p == q:
                return p
            p, q = p.next, q.next
        return None

    def getIntersectionNode2(self, headA, headB):
        pa, pb = headA, headB

        if not pa or not pb:
            return None

        while pa != pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa
