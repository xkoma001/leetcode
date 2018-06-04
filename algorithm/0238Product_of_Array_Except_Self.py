class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m_len = len(nums)
        res = [1] * m_len

        for i in range(1, m_len):
            res[i] = res[i-1] * nums[i-1]
        right = 1
        for i in range(m_len-2, -1, -1):
            right *= nums[i+1]
            res[i] *= right
        return res
