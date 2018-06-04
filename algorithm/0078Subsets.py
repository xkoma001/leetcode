class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for num in nums:
            cur_rel = []
            for cur in ans:
                cur_rel.append(cur+[num])
            ans = ans + cur_rel
        return ans

    def subsets2(self, nums):
        m_len = len(nums)
        kinds = 2 ** m_len
        ans = [[] for _ in range(kinds)]
        for i in range(kinds):
            for j in range(m_len):
                if (i >> j) & 1:
                    ans[i].append(nums[j])
        return ans
