class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def combination(can, path, i, cur_sum):
            if cur_sum == target:
                ans.append(path)
                return

            if i == len(can):
                return

            combination(can, path, i+1, cur_sum)
            if i == 0 or (can[i] == can[i-1] and used[i-1]) or can[i] != can[i-1]:
                if can[i] + cur_sum <= target:
                    used[i] = True
                    combination(can, path+[can[i]], i+1, cur_sum+can[i])
                    used[i] = False

        candidates.sort()
        ans = []
        used = [False] * len(candidates)
        combination(candidates, [], 0, 0)
        return ans

if __name__ == '__main__':
    l = [1]
    target = 1
    s = Solution()
    print(s.combinationSum2(l, target))
