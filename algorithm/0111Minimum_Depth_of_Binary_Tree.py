# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def min_depth(root):
            if root:
                if root.left and root.right:
                    return min(min_depth(root.left), min_depth(root.right))+1
                elif root.left:
                    return min_depth(root.left) + 1
                elif root.right:
                    return min_depth(root.right) + 1
                else:
                    return 1
            return 0
        return min_depth(root)
