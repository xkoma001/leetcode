# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def tree_height(self, root):
        if not root:
            return 0
        left = self.tree_height(root.left)
        right = self.tree_height(root.right)
        return max(left, right)+1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        h1 = self.tree_height(root.left)
        h2 = self.tree_height(root.right)

        return abs(h1-h2) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def sub_height(self, node):
        if not node:
            return 0
        left = self.sub_height(node.left)
        if left == -1:
            return -1
        right = self.sub_height(node.right)
        if right == -1:
            return -1
        if abs(left-right) > 1:
            return -1
        return max(left, right)+1

    def isBalanced2(self, root):
        return self.sub_height(root) != -1
