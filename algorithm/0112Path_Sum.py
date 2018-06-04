# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        def path_sum(node, cur_sum):
            if not node:
                return False
            else:
                cur_sum += node.val
                if node.left and node.right:
                    return path_sum(node.left, cur_sum) or path_sum(node.right, cur_sum)
                elif node.left:
                    return path_sum(node.left, cur_sum)
                elif node.right:
                    return path_sum(node.right, cur_sum)
                else:
                    return cur_sum == sum

        return path_sum(root, 0)
