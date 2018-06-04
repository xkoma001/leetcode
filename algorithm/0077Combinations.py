class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        coms = [i for i in range(1, n+1)]
        ans = []

        def comb(remains, cur_rel, k):
            if not k and cur_rel:
                ans.append(cur_rel)
                return

            for pos, val in enumerate(remains):
                comb(remains[pos+1:], cur_rel+[val], k-1)
            return

        comb(coms, [], k)
        return ans

    def combine2(self, n, k):
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n - k + l + 1:
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1

if __name__ == '__main__':
    s = Solution()
    print(s.combine2(4, 2))