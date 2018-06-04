class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res, m_len, closet = [], len(nums), None
        closet_num, dis = 0, None
        nums.sort()
        print(nums)
        for i in range(m_len - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                l, r = i + 1, m_len-1
                while l < r:
                    new_sum = nums[i] + nums[l] + nums[r]

                    if new_sum == target:
                        return new_sum
                    elif new_sum < target:
                        dis = target - new_sum
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        l += 1
                    else:
                        dis = new_sum - target
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        r -= 1
                    if closet is None:
                        closet = dis
                        closet_num = new_sum
                    closet_num = new_sum if dis < closet else closet_num
                    closet = dis if dis < closet else closet
        return closet_num

if __name__ == '__main__':
    s = Solution()
    nums = [-1,0,1,1,55]
    print(s.threeSumClosest(nums, 3))
