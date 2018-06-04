# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        1. 遍历两遍，应该超时
        2. 双指针思路只遍历一遍
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not n:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        cur_node = dummy

        node_len = 0
        while cur_node:
            node_len += 1
            cur_node = cur_node.next
        m = node_len - n

        cur_node = dummy
        while cur_node and m > 1:
            m -= 1
            cur_node = cur_node.next
        cur_node.next = cur_node.next.next
        return dummy.next

    def removeNthFromEnd2(self, head, n):
        if not n:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy
        step = 0

        while fast.next:
            step += 1
            if step >= n+1:
                slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next
