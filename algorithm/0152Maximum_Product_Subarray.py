class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_product = nums[0]
        pre = (nums[0], nums[0])
        for num in nums[1:]:
            cur_min = min(num, num*pre[0], num*pre[1])
            cur_max = max(num, num*pre[0], num*pre[1])
            pre = (cur_min, cur_max)
            max_product = max(max_product, cur_max)
        return max_product
