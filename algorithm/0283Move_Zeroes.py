class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        m_len = len(nums)
        start = 0
        for i in range(m_len):
            if nums[i] != 0:
                nums[start] = nums[i]
                start += 1

        for i in range(start, m_len):
            nums[i] = 0

        return
