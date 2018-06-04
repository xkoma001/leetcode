class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        timeout
        """
        m = len(nums)
        achieve = [False]*m
        achieve[0] = True
        for i, val in enumerate(nums):
            if achieve[i]:
                if i+val >= m-1:
                    return True
                for j in range(i+1, i+val+1):
                    achieve[j] = True

        return False

    def canJump2(self, nums):
        if not nums:
            return True
        m_len = len(nums)
        reach = m_len-1
        for i in range(m_len-2, -1, -1):
            if i+nums[i] >= reach:
                reach = i
        return reach == 0
