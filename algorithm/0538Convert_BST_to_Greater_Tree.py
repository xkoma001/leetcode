# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def travel(self, pre, root):
        if not root:
            return pre

        cur_val = self.travel(pre, root.right)
        root.val += cur_val
        return self.travel(root.val, root.left)

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        pre = 0
        self.travel(pre, root)
        return root
