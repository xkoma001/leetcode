__author__ = 'xkoma'


class Solution:
    def threeSum(self, nums):
        """
        思路１:
        暴力法
        时间复杂度为O(n^3)
        思路2:
        复杂度过高可以优先排序，排序后
        利用有序元素的特性，时间复杂度为O(n^2)
        pass
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        m_len = len(nums)
        cur_sum, rv = 0, []
        for i in range(0, m_len-2):
            for j in range(i+1, m_len-1):
                for k in range(j+1, m_len):
                    cur_sum = nums[i] + nums[j] + nums[k]
                    if cur_sum == 0:
                        rel = sorted([nums[i], nums[j], nums[k]])
                        if rel not in rv:
                            rv.append(rel)
                    else:
                        cur_sum = 0

        return rv

    def threeSum2(self, nums):
        res, m_len = [], len(nums)
        nums.sort()
        for i in range(m_len-2):
            if i == 0 or nums[i] != nums[i-1]:
                l, r, sum = i+1, m_len-1, -nums[i]
                while l < r:
                    new_sum = nums[l] + nums[r]
                    if new_sum == sum:
                        res.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif new_sum < sum:
                        l += 1
                    else:
                        r -= 1

        return res

if __name__ == '__main__':
    s = Solution()
    nums = [-1, -1, 2, -4]
    print(s.threeSum2(nums))
