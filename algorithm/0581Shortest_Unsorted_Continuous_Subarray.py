class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        m_len = len(nums)
        nums_sorted = sorted(nums)
        i, j = 0, m_len-1

        while i < m_len and nums[i] == nums_sorted[i]:
            i += 1
        while i < j and nums[j] == nums_sorted[j]:
            j -= 1

        return j-i+1
