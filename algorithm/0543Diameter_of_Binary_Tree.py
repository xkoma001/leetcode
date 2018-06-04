# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        max_dia = 0

        def long_tree(node, depth):
            if not node:
                return depth

            left = long_tree(node.left, depth+1) if node.left else depth
            right = long_tree(node.right, depth+1) if node.right else depth

            return left if left > right else right

        def diameter_tree(node):
            if not node:
                return 0
            nonlocal max_dia

            left = long_tree(node.left, 1) if node.left else 0
            right = long_tree(node.right, 1) if node.right else 0
            max_dia = max(left+right, max_dia)

            diameter_tree(node.left)
            diameter_tree(node.right)
            return

        diameter_tree(root)
        return max_dia

    def diameterOfBinaryTree2(self, root):
        max_dia = 0

        def max_depth(node):
            nonlocal max_dia
            if not node:
                return 0
            left = max_depth(node.left)
            right = max_depth(node.right)
            max_dia = max(max_dia, left+right)
            return max(left, right) + 1
        max_depth(root)
        return max_dia


