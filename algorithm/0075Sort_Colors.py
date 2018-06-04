class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        for i, val in enumerate(nums):
            for j in range(i-1, -1, -1):
                if nums[j] <= val:
                    nums[j+1] = val
                    break
                nums[j+1] = nums[j]
                if j == 0:
                    nums[j] = val
        return

    def sortColors2(self, nums):
        i = j = 0
        for k in range(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1
        return

