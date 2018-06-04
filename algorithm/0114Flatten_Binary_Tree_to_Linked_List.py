# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        if not root.left:
            return self.flatten(root.right)
        if not root.right:
            root.right = root.left
            root.left = None
            return self.flatten(root.right)

        prev_node = root.left
        while prev_node.right:
            prev_node = prev_node.right
        prev_node.right = root.right
        root.right = root.left
        root.left = None
        return self.flatten(root.right)

    def flatten2(self, root):
        if not root:
            return

        cur = root
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right:
                    pre = pre.right
                pre.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right
        return




        pass
