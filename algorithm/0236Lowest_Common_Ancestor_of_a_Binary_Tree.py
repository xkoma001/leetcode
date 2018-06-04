# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def ancestor(parent, node, path, rel):
            path.append(parent)
            if parent == node:
                rel.extend(path)
                return
            if parent.left:
                ancestor(parent.left, node, path, rel)
            if parent.right:
                ancestor(parent.right, node, path, rel)
            path.pop()
            return

        if not root:
            return root
        elif not p:
            return q
        elif not q:
            return p

        p_path, q_path = [], []
        ancestor(root, p, [], p_path)
        ancestor(root, q, [], q_path)
        p_len, q_len = len(p_path), len(q_path)
        i = 0

        while i < p_len and i < q_len and p_path[i] == q_path[i]:
            i += 1
        return p_path[i-1]

    def lowestCommonAncestor2(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor2(root.left, p, q)
        right = self.lowestCommonAncestor2(root.right, p, q)
        if left and right:
            return root
        return left if left else right
