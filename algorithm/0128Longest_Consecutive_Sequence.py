class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}
        long = 0
        for num in nums:
            if num in memo:
                continue
            left = memo[num-1] if num-1 in memo else 0
            right = memo[num+1] if num+1 in memo else 0
            total = left + right + 1
            long = max(long, total)
            memo[num] = total
            memo[num-left] = total
            memo[num+right] = total
        return long
