class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        m_len = len(s)

        def check_word(l, h):
            if l > h:
                return True

            for m in range(l, h+1):
                if s[l:m+1] in wordDict and check_word(m+1, h):
                    return True
            return False
        return check_word(0, m_len-1)

    def wordBreak2(self, s, wordDict):
        m_len = len(s)

        dp = [[0] * m_len for _ in range(m_len)]

        for i in range(m_len):
            for j in range(i, m_len):
                if s[i:j+1] in wordDict:
                    dp[i][j] = 1
                else:
                    for k in range(i, j):
                        if dp[i][k] and s[k+1:j+1] in wordDict:
                            dp[i][j] = 1
                            break

        return True if dp[0][m_len-1] else False

    def wordBreak3(self, s, wordDict):
        m_len = len(s)
        dp = [False] * m_len

        for i in range(m_len):
            if s[:i+1] in wordDict:
                dp[i] = True
                continue
            for j in range(i-1, -1, -1):
                if dp[j] and s[j+1:i+1] in wordDict:
                    dp[i] = True
                    break
        return dp[m_len-1]
