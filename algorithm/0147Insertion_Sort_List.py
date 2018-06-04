# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        pre = dummy = ListNode(0)
        dummy.next = head
        cur = head

        while cur.next:
            compare = cur.next
            if pre.next.val >= compare.val:
                pre = dummy
            while pre.next != compare and pre.next.val < compare.val:
                pre = pre.next
            if pre.next == compare:
                cur = cur.next
            else:
                cur.next = compare.next
                compare.next = pre.next
                pre.next = compare
        return dummy.next

    def insertionSortList2(self, head):
        if not head:
            return head

        cur = dummy = ListNode(0)
        while head:
            if cur.val >= head.val:
                cur = dummy
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            cur.next, cur.next.next, head = head, cur.next, head.next
        return dummy.next
