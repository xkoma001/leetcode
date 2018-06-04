# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []

        def path_sum(node, paths, sum):
            if not node:
                return False
            else:
                sum -= node.val
                paths.append(node.val)
                if not node.left and not node.right and sum == 0:
                    ans.append(paths[:])
                path_sum(node.left, paths, sum)
                path_sum(node.right, paths, sum)
                paths.pop()
            return
        path_sum(root, [], sum)
        return ans

    def pathSum2(self, root, sum):
        ans = []
        if not root:
            return ans

        stack = [(root, [root.val], root.val)]
        while stack:
            cur_node, paths, rel = stack.pop()
            if cur_node.right:
                stack.append((cur_node.right, paths+[cur_node.right.val], rel+cur_node.right.val))
            if cur_node.left:
                stack.append((cur_node.left, paths+[cur_node.left.val], rel+cur_node.left.val))
            if not cur_node.left and not cur_node.right and rel == sum:
                    ans.append(paths[:])
        return ans


