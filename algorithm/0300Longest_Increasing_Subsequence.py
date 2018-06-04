class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m_len = len(nums)
        if not m_len:
            return 0
        longest = 1
        dp = [1]*m_len

        for i in range(1, m_len):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            longest = max(dp[i], longest)
        return longest

    def lengthOfLIS2(self, nums):
        m_len = len(nums)
        tails = [0]*m_len
        size = 0
        for num in nums:
            if size == 0:
                tails[0] = num
                size += 1
            elif num <= tails[0]:
                tails[0] = num
            elif num > tails[size-1]:
                tails[size] = num
                size += 1
            else:
                i, j = 0, size-1
                while i < j:
                    mid = (i+j)//2
                    if tails[mid] < num:
                        i = mid+1
                    else:
                        j = mid
                tails[i] = num

        return size
