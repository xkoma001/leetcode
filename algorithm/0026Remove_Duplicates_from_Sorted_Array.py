class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        p = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[p] = nums[i]
                p += 1

        return p

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,2]))