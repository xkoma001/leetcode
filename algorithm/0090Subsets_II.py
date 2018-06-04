class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        nums.sort()

        pre = 0
        for i, num in enumerate(nums):
            cur_len = len(ans)
            if i != 0 and num == nums[i-1]:
                cur_ans = ans[pre:]
            else:
                cur_ans = ans[:]
            for cur in cur_ans:
                ans.append(cur+[num])
            pre = cur_len

        return ans

    def subsetsWithDup2(self, nums):
        ans = []
        num_len = len(nums)
        nums.sort()

        def sub_with_dup(nums, begin, path):
            ans.append(path[:])
            for i in range(begin, num_len):
                if i == begin or nums[i] != nums[i-1]:
                    path.append(nums[i])
                    sub_with_dup(nums, i+1, path)
                    path.pop()
            return

        sub_with_dup(nums, 0, [])
        return ans

    def subsetsWithDup3(self, S):
        res = [[]]
        S.sort()
        for i in range(len(S)):
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [S[i]])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup3([1, 2, 2, 2]))
