# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def mirror_tree(left, right):
            if not left and not right:
                return True

            if left and right and left.val == right.val:
                return mirror_tree(left.left, right.right) and mirror_tree(left.right, right.left)
            return False

        if not root:
            return True
        return mirror_tree(root.left, root.right)

    def isSymmetric2(self, root):
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop(0)
            if not left and not right:
                continue
            if left and right and left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True


        pass
