# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        while head:
            cur_node = head
            head = head.next
            cur_node.next = dummy.next
            dummy.next = cur_node
        return dummy.next

    def reverseList2(self, head):
        if not head or not head.next:
            return head

        old_head = head
        while head.next.next:
            head = head.next
        new_head = head.next
        head.next = None
        new_head.next = self.reverseList2(old_head)
        return new_head

    def reverseList3(self, head):
        new_head = None

        def reverse_list(head):
            nonlocal new_head
            if not head:
                return None
            next_node = head.next
            head.next = new_head
            new_head = head
            head = next_node
            return reverse_list(head)

        reverse_list(head)
        return new_head
