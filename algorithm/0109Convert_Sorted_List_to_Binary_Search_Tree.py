# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        cur_len, cur_node = 0, head

        while cur_node:
            cur_len += 1
            cur_node = cur_node.next

        def helper(node, length):
            if length < 1:
                return None

            low, high = 0, length-1
            mid = (low+high) // 2
            cur = node
            for _ in range(mid-1):
                cur = cur.next

            if mid != 0:
                prev_node = cur
                mid_node = prev_node.next
            else:
                mid_node = cur

            next_node = mid_node.next
            root = TreeNode(mid_node.val)
            root.left = helper(node, mid)
            root.right = helper(next_node, length-1-mid)
            return root

        return helper(head, cur_len)

