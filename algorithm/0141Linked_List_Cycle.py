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
        slow, fast = head, head

        while fast:
            fast = fast.next
            if fast == slow:
                return True
            if fast:
                fast = fast.next
                if fast == slow:
                    return True
            slow = slow.next
        return False

    def hasCycle2(self, head):
        if not head:
            return False
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

