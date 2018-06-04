__author__ = 'xkoma'


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        def perm(remains, rv):
            if not remains:
                ans.append(rv[:])
                return
            for i, val in enumerate(remains):
                if i == 0 or val not in remains[:i]:
                    rv.append(val)
                    new_list = remains[:]
                    new_list.remove(val)
                    perm(new_list, rv)
                    rv.pop()
        perm(nums, [])
        return ans

    def permuteUnique2(self, nums):
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l) + 1):
                    new_ans.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i] == n: break  # handles duplication
            ans = new_ans
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique2([1,2,1]))
