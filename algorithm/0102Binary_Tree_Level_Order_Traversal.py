# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans, stack = [], [(root, 1)]
        cur_layer = 0
        while stack:
            node, layer = stack.pop(0)
            if layer != cur_layer:
                ans.append([])
                cur_layer += 1
            if node.left:
                stack.append((node.left, cur_layer+1))
            if node.right:
                stack.append((node.right, cur_layer+1))
            ans[layer-1].append(node.val)
        return ans
