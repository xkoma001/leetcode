# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        first, second = head, head.next
        prev = dummy
        while first and second:
            third = second.next
            prev.next = second
            second.next = first
            first.next = third
            prev = first
            if third:
                first, second = third, third.next
            else:
                first, second = None, None

        return dummy.next

if __name__ == '__main__':
    s = Solution()
    from utils import make_link, travel_list
    l = [1, 2, 3, 4]
    new = make_link(l)
    rel = s.swapPairs(new)
    print(travel_list(rel))
