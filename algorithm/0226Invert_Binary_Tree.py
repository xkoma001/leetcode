# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root

    def invertTree2(self, root):
        if not root:
            return root
        stack = [root]

        while stack:
            cur_node = stack.pop()
            left, right = cur_node.left, cur_node.right
            cur_node.left = right
            cur_node.right = left
            if right:
                stack.append(right)
            if left:
                stack.append(left)
        return root
