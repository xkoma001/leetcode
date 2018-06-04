class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        m_len = len(nums)
        ans = []
        for i in range(m_len):
            while nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(m_len):
            if nums[i] != i+1:
                ans.append(i+1)
        return ans

    def findDisappearedNumbers2(self, nums):
        m_len = len(nums)
        ans = []
        for i in range(m_len):
            index = abs(nums[i])-1
            if nums[index] > 0:
                nums[index] = -nums[index]
        for i in range(m_len):
            if nums[i] > 0:
                ans.append(i+1)
        return ans
