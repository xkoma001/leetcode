class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        cur = nums[0]
        for num in nums[1:]:
            cur ^= num
        return cur


