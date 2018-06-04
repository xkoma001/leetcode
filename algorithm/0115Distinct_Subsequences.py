class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        if m < n:
            return 0

        rel = [[0] * n for _ in range(m)]

        for j in range(n):
            for i in range(j, m):
                if i > 0:
                    rel[i][j] += rel[i-1][j]
                if s[i] == t[j]:
                    if j == 0:
                        rel[i][j] += 1
                    else:
                        rel[i][j] += rel[i-1][j-1]
        return rel[m-1][n-1]

if __name__ == '__main__':
    s = Solution()
    print(s.numDistinct("bbi", "bi"))
