# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        ans = []
        stack = [root]
        drec = 1

        while stack:
            if drec:
                cur_rel = [node.val for node in stack]
                drec = 0
            else:
                cur_rel = [node.val for node in stack[::-1]]
                drec = 1
            ans.append(cur_rel)
            stack = [kid for pair in stack for kid in (pair.left, pair.right) if kid]
        return ans



