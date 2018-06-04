# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        longest = float('-Inf')

        def long_path(node):
            if not node:
                return 0
            nonlocal longest
            left = long_path(node.left)
            right = long_path(node.right)
            cur = 0
            if left > 0:
                cur += left
            if right > 0:
                cur += right
            cur += node.val
            longest = max(longest, cur)
            return max(node.val+left, node.val+right, node.val)
        long_path(root)
        return longest
