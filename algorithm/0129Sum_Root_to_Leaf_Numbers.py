# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        total = 0
        paths, stack = [], [(root, root.val)]
        while stack:
            cur, cur_sum = stack.pop()
            if not cur.left and not cur.right:
                total += cur_sum
                continue
            base = cur_sum * 10
            if cur.right:
                stack.append((cur.right, base+cur.right.val))
            if cur.left:
                stack.append((cur.left, base+cur.left.val))
        return total
