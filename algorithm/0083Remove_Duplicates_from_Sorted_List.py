# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        first, second = head, head.next

        while second:
            if second.val == first.val:
                second = second.next
                first.next = second
            else:
                first = second
                second = second.next
        return head
