# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        totals = 0

        def travel_start(node):
            if not node:
                return 0

            path_start(0, node)
            travel_start(node.left)
            travel_start(node.right)
            return

        def path_start(pre, node):
            if not node:
                return
            if (pre+node.val) == sum:
                nonlocal totals
                totals += 1
            path_start(pre+node.val, node.left)
            path_start(pre+node.val, node.right)

        travel_start(root)
        return totals

    def pathSum2(self, root, sum):
        from collections import defaultdict
        hash_map = defaultdict(int)
        hash_map[0] = 1

        def check_sum(node, sum, target):
            if not node:
                return 0

            cur_sum = sum + node.val
            res = hash_map[cur_sum-target]
            hash_map[cur_sum] += 1
            res += check_sum(node.left, cur_sum, target) + check_sum(node.right, cur_sum, target)
            hash_map[cur_sum] -= 1
            return res

        return check_sum(root, 0, sum)
