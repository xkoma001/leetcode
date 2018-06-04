class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        cur_num, repeat = nums[0], 1
        i, j = 1, 1
        while j < len(nums):
            if nums[j] != cur_num:
                repeat = 1
                cur_num = nums[i] = nums[j]
                i += 1
            elif repeat == 2:
                pass
            else:
                repeat += 1
                nums[i] = nums[j]
                i += 1
            j += 1
        return i

    def removeDuplicates2(self, nums):
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1

        return i

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1]))
