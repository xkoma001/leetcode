# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if not nums:
            return None
        mid = (len(nums)-1) // 2
        cur_node = TreeNode(nums[mid])
        cur_node.left = self.sortedArrayToBST(nums[:mid])
        cur_node.right = self.sortedArrayToBST(nums[mid+1:])
        return cur_node
