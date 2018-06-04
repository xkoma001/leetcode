class Solution:
    def searchInsert(self, nums, target):
        """
        O(n)
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0
        for i in range(len(nums)):
            if nums[i] >= target:
                break
            index += 1
        return index

    def searchInsert2(self, nums, target):
        """
        O(logn)
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        if r < 0:
            return 0

        while l < r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        if nums[l] >= target:
            return l
        else:
            return l+1
