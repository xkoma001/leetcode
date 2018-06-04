class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans, m_len = [], len(nums)
        if m_len < 4:
            return ans

        nums.sort()
        for i in range(m_len-3):
            if i == 0 or nums[i] != nums[i-1]:
                f_sum = target-nums[i]
                for j in range(i+1, m_len-2):
                    if j == i+1 or nums[j] != nums[j-1]:
                        l, r = j+1, m_len-1
                        to_sum = f_sum - nums[j]
                        while l < r:
                            new_sum = nums[l] + nums[r]
                            if new_sum == to_sum:
                                ans.append([nums[i], nums[j], nums[l], nums[r]])
                                while l < r and nums[l] == nums[l + 1]:
                                    l += 1
                                while l < r and nums[r] == nums[r - 1]:
                                    r -= 1
                                l += 1
                                r -= 1
                            elif new_sum < to_sum:
                                l += 1
                            else:
                                r -= 1
        return ans