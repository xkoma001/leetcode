__author__ = 'xkoma'


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []

        def combination(candidates, cur_rel, cur_sum):
            if cur_sum == target:
                ans.append(cur_rel)
                return
            if candidates:
                combination(candidates[1:], cur_rel, cur_sum)
                count = 0
                while cur_sum + candidates[0] <= target:
                    count += 1
                    cur_sum += candidates[0]
                    combination(candidates[1:], cur_rel+[candidates[0]]*count, cur_sum)
            return

        combination(candidates, [], 0)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))
    pass