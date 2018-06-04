class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        low, high = 0, n-1
        mid = (low + high) // 2

        while low <= high:
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                high = mid - 1
                mid = (low + high) // 2
            else:
                low = mid + 1
                mid = (low + high) // 2

        if low > high:
            return [-1, -1]
        start, end = mid, mid
        while start > 0 and nums[start-1] == target:
            start -= 1
        while end < n-1 and nums[end+1] == target:
            end += 1
        return [start, end]
