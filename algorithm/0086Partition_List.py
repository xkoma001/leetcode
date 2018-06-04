# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        small, big = ListNode(0), ListNode(1)

        cur_small, cur_big = small, big
        while head:
            if head.val < x:
                cur_small.next = head
                cur_small = cur_small.next
            else:
                cur_big.next = head
                cur_big = cur_big.next
            head = head.next
        cur_small.next = big.next
        cur_big.next = None
        return small.next
