class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(32):
            sum = 0
            for num in nums:
                if (num >> i) & 1 == 1:
                    sum += 1
            sum %= 3
            ans |= sum << i
        ans = ans - (1 << 32) if ans >= (1 << 31) else ans
        return ans
