# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans, stack = [], [root]

        while stack:
            cur_rel = [node.val for node in stack]
            stack = [kid for pair in stack for kid in (pair.left, pair.right) if kid]
            ans.insert(0, cur_rel)

        return ans
