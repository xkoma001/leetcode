class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        g = [0 for _ in range(n+1)]
        g[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                g[i] += g[j] * g[i-j-1]
        return g[n]
