class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = {}

        def is_pair(s):
            return s == s[::-1]

        def helper(s, left_cut):
            if left_cut == 0:
                if s not in memo and is_pair(s):
                    return True
                else:
                    memo[s] = 1
                    return False

            if left_cut > 0:
                left_cut -= 1
                for i in range(len(s)-left_cut-1):
                    if s[:i+1] not in memo and is_pair(s[:i+1]):
                        if helper(s[i+1:], left_cut):
                            return True
                    else:
                        memo[s[:i+1]] = 1

            return False

        for cut in range(0, len(s)):
            if helper(s, cut):
                return cut

    def minCut2(self, s):
        if not s:
            return 0

        n = len(s)
        d = [n] * n
        pair = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i < 2 or pair[i+1][j-1]):
                    if j == n-1:
                        d[i] = 0
                    else:
                        d[i] = min(d[j+1]+1, d[i])
                    pair[i][j] = True
        return d[0]
