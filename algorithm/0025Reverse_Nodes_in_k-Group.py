# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        s, e = dummy, head
        while e:
            count = 1
            while count < k and e.next:
                tmp = e.next
                e.next = tmp.next
                tmp.next = s.next
                s.next = tmp
                count += 1

            if 1 < count < k:  # reverse back
                e = s.next
                while e.next:
                    tmp = e.next
                    e.next = tmp.next
                    tmp.next = s.next
                    s.next = tmp
                break
            s, e = e, e.next

        return dummy.next
