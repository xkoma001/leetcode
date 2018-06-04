class Solution:
    def reverse(self, nums, i, j):
        swap_len = (j-i+1)//2
        for m in range(swap_len):
            nums[i+m], nums[j-m] = nums[j-m], nums[i+m]
        return

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        m_len = len(nums)
        j, k = m_len-2, m_len-1

        while j >= 0:
            if nums[j] < nums[k]:
                l = k
                while l <= m_len-2 and nums[l+1] > nums[j]:
                    l += 1
                nums[j], nums[l] = nums[l], nums[j]
                self.reverse(nums, k, m_len-1)
                return
            else:
                j -= 1
                k -= 1
        self.reverse(nums, k, m_len-1)
        return
