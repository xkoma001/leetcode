# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        cur_node = dummy
        for _ in range(m-1):
            cur_node = cur_node.next
        pre_m = cur_node
        cur_node = cur_node.next
        prev_node = rev_node = cur_node

        for _ in range(n-m+1):
            next_node = cur_node.next
            cur_node.next = rev_node
            rev_node = cur_node
            cur_node = next_node
        prev_node.next = cur_node
        pre_m.next = rev_node
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5]
    from utils import make_link, travel_list
    print(travel_list(s.reverseBetween(make_link(nums), 2, 4)))
