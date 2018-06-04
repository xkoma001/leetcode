# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if p and q and p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        return False

    def isSameTree2(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False

        stack = [p, q]
        while len(stack):
            p = stack.pop()
            q = stack.pop()
            if p.val != q.val:
                return False
            if (p.left and not q.left) or (not p.left and q.left):
                return False
            if p.left and q.left:
                stack += [p.left, q.left]

            if (p.right and not q.right) or (not p.right and q.right):
                return False
            if p.right and q.right:
                stack += [p.right, q.right]

        return True
