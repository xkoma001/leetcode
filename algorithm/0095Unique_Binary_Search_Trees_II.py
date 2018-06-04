# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        nums = [i for i in range(1, n+1)]

        def gen_trees(nums):
            if not nums:
                return [None]
            ans = []
            for i, num in enumerate(nums):
                for left in gen_trees(nums[:i]):
                    for right in gen_trees(nums[i+1:]):
                        root = TreeNode(num)
                        root.left = left
                        root.right = right
                        ans.append(root)
            return ans

        return gen_trees(nums) if n > 0 else []
