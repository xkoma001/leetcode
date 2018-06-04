class Solution:
    def removeElement(self, nums, val):
        """
        思路１：
        左移动ｎ位
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        total_len = len(nums)
        index, rem_num = 0, 0

        while index <= (total_len-1):
            if nums[index] == val:
                rem_num += 1
            elif rem_num:
                nums[index-rem_num] = nums[index]
            index += 1

        return total_len-rem_num

if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([2,3,3,2], 2))
