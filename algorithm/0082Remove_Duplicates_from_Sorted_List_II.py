# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = dummy = ListNode(0)
        while head:
            repeat = head.val
            if head.next and head.next.val == repeat:
                while head and head.val == repeat:
                    head = head.next
            else:
                pre.next = head
                head = head.next
                pre = pre.next
                pre.next = None

        return dummy.next

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 2]
    from utils import make_link, travel_list
    print(travel_list(s.deleteDuplicates(make_link(nums))))
