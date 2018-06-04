# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ans, stack = [], [(root, 0)]

        while stack:
            cur, st = stack.pop()
            if st == 1:
                ans.append(cur.val)
            else:
                stack.append((cur, 1))
                if cur.right:
                    stack.append((cur.right, 0))
                if cur.left:
                    stack.append((cur.left, 0))
        return ans

    def postorderTraversal2(self, root):
        if not root:
            return []
        stack, ans = [root], []
        while stack:
            cur = stack.pop()
            ans.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return ans[::-1]


