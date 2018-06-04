class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        m_len = len(s)
        totals = 0
        hash_pal = {}

        def is_pal(a):
            return a == a[::-1]

        for i in range(m_len):
            for j in range(i, m_len):
                if s[i:j+1] in hash_pal:
                    totals += 1
                elif is_pal(s[i:j+1]):
                    hash_pal[s[i:j+1]] = 1
                    totals += 1
        return totals

    def countSubstrings2(self, s):
        m_len = len(s)
        dp = [[0]*m_len for _ in range(m_len)]
        totals = 0

        for i in range(m_len-1, -1, -1):
            for j in range(i, m_len):
                if s[i] == s[j] and (j-i < 3 or dp[i+1][j-1]):
                    dp[i][j] = 1
                    totals += 1
        return totals

    def countSubstrings3(self, s):
        m_len = len(s)
        totals = 0

        def check_pair(i, j):
            while i >= 0 and j < m_len and s[i] == s[j]:
                nonlocal totals
                i -= 1
                j += 1
                totals += 1

        for i in range(m_len):
            check_pair(i, i)
            check_pair(i, i+1)
        return totals
