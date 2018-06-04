class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k == 0:
            return []
        from collections import deque
        cur_max = nums[0]
        ans, d = [], deque()

        for num in nums[:k]:
            cur_max = max(num, cur_max)
            d.append(num)

        ans.append(cur_max)
        for num in nums[k:]:
            first = d.popleft()
            d.append(num)
            if num >= cur_max:
                cur_max = num
                ans.append(num)
            elif cur_max != first:
                ans.append(cur_max)
            else:
                cur_max = d[0]
                for new_num in d:
                    cur_max = max(cur_max, new_num)
                ans.append(cur_max)

        return ans

    def maxSlidingWindow2(self, nums, k):
        if not nums or k == 0:
            return []
        from collections import deque
        ans, d = [], deque()
        for i in range(len(nums)):
            while d and d[0] < i-k+1:
                d.popleft()
            while d and nums[i] > nums[d[-1]]:
                d.pop()
            d.append(i)
            if i >= k-1:
                ans.append(nums[d[0]])
        return ans
