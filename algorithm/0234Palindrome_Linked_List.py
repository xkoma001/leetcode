# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        fast, slow = head, head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = rev
            rev = slow
            slow = tmp

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
        return True if rev is None else False
