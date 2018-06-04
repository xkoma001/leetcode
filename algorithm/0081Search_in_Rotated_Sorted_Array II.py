class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        m_len = len(nums)
        low, high = 0, m_len-1

        while low <= high:
            mid = (low+high) >> 1
            if nums[mid] == target:
                return True
            elif nums[low] <= nums[mid]:
                if nums[low] == nums[mid]:
                    low += 1
                elif nums[mid] > target >= nums[low]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return False
