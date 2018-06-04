class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        m_len = len(nums)
        for i in range(m_len):
            while 0 < nums[i] <= m_len and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        place = 0
        for i in range(m_len):
            if nums[i] != i+1:
                place = i+1
                return place

        place = m_len + 1
        return place
