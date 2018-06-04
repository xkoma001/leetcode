__author__ = 'xkoma'


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        def perm(remains, rv):
            if not remains:
                ans.append(rv[:])
                return
            for val in remains:
                rv.append(val)
                new_list = remains[:]
                new_list.remove(val)
                perm(new_list, rv)
                rv.pop()

        perm(nums, [])
        return ans

    def permute2(self, nums):
        from functools import reduce
        return reduce(lambda P,n: [p[:i]+[n]+p[i:] for p in P for i in range(len(p)+1)],
                      nums, [[]])


if __name__ == '__main__':
    s = Solution()
    print(s.permute2([1,3,2]))
