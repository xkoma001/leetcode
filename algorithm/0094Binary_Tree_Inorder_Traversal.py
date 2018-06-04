# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []

        def inorder(root):
            if not root:
                return

            if root.left:
                inorder(root.left)
            ans.append(root.val)
            if root.right:
                inorder(root.right)
            return
        inorder(root)
        return ans

    def inorderTraversal2(self, root):
        if not root:
            return []
        ans, stack = [], [(root, 0)]
        while len(stack):
            cur = stack.pop()
            root, st = cur
            if st == 1:
                ans.append(root.val)
                continue
            if root.right:
                stack.append((root.right, 0))
            if st == 0:
                stack.append((root, 1))
            if root.left:
                stack.append((root.left, 0))
        return ans

    def inorder_morris(self, root):
        ans = []
        cur = root
        while cur:
            if not cur.left:
                ans.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if pre.right == cur:
                    ans.append(cur.val)
                    cur = cur.right
                elif not pre.right:
                    pre.right = cur
                    cur = cur.left
        return ans






