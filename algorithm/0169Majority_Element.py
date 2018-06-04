class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        from collections import defaultdict
        ems = defaultdict(int)
        num_len = len(nums)
        mid_len = num_len//2+1 if num_len % 2 != 0 else num_len//2
        for num in nums:
            ems[num] += 1
            if ems[num] >= mid_len:
                return num

    def majorityElement2(self, nums):
        rel, count = nums[0], 1
        for num in nums[1:]:
            if count == 0:
                rel = num
                count += 1
            elif num == rel:
                count += 1
            else:
                count -= 1
        return rel
