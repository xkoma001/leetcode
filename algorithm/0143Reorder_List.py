# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        new_head = head
        while new_head:
            first, second = new_head, new_head.next
            if not second or not second.next:
                break

            pre_last = second
            while pre_last.next.next:
                pre_last = pre_last.next
            last = pre_last.next
            pre_last.next = None
            first.next = last
            last.next = second
            new_head = second
        return

    def reorderList2(self, head):
        if not head or not head.next:
            return

        rel, l_len = [], 0
        while head:
            l_len += 1
            rel.append(head)
            head = head.next

        i, j = 0, l_len-1
        pre = ListNode(0)
        while i <= j:
            if i == j:
                pre.next = rel[i]
            else:
                rel[i].next = rel[j]
                pre.next = rel[i]
            pre = rel[j]
            i += 1
            j -= 1
        pre.next = None
        return

    def reorderList3(self, head):
        if not head or not head.next or not head.next.next:
            return

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        first, second = slow, slow.next

        first.next = None
        rev = second.next
        second.next = None
        while rev:
            tmp = rev.next
            rev.next = second
            second = rev
            rev = tmp

        pre = None
        p1, p2 = head, second
        while p1:
            tmp_1 = p1.next
            if p2:
                tmp_2 = p2.next
            p1.next = p2
            if pre:
                pre.next = p1
            pre = p2
            p1, p2 = tmp_1, tmp_2

        return
