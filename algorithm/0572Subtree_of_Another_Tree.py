# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def is_same(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val == t.val and self.is_same(s.left, t.left) and self.is_same(s.right, t.right):
            return True
        return False

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        if not s:
            return False

        if self.is_same(s, t):
            return True
        elif self.isSubtree(s.left, t) or self.isSubtree(s.right, t):
            return True
        else:
            return False
