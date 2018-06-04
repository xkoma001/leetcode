# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        fast, slow = head, head
        step = 0

        cur_node = head
        m_len = 0
        while cur_node:
            m_len += 1
            cur_node = cur_node.next
        k = k % m_len if m_len != 0 else 0

        if k <= 0 or not head:
            return head

        while fast.next and step < k:
            fast = fast.next
            step += 1

        if not fast.next and step != k:
            return head

        while fast.next:
            fast = fast.next
            slow = slow.next

        new_head = slow.next
        slow.next = fast.next
        fast.next = head
        return new_head
