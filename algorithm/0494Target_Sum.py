class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        totals = 0
        i, m_len = 0, len(nums)

        def depth(i, cur_sum):
            nonlocal totals
            if i == m_len:
                if cur_sum == S:
                    totals += 1
                return

            depth(i+1, cur_sum+nums[i])
            depth(i+1, cur_sum-nums[i])
        depth(0, 0)
        return totals

    def findTargetSumWays2(self, nums, S):
        if not nums:
            return 0
        totals = 0
        i, m_len = 0, len(nums)
        stack = [(0, nums[0]), (0, -nums[0])]

        while stack:
            pair = stack.pop()
            if pair[0] == m_len-1:
                if pair[1] == S:
                    totals += 1
            else:
                stack.append((pair[0]+1, pair[1]+nums[pair[0]+1]))
                stack.append((pair[0]+1, pair[1]-nums[pair[0]+1]))
        return totals

    def findTargetSumWays3(self, nums, S):
        total_sum = sum(nums)
        if total_sum < S or -total_sum > S:
            return 0

        def sub_sum(nums, s):
            dp = [0]*(s+1)
            dp[0] = 1
            for num in nums:
                for i in range(s, num-1, -1):
                    dp[i] += dp[i-num]
            return dp[s]

        return 0 if (S+total_sum) & 1 else sub_sum(nums, (S+total_sum) >> 1)
