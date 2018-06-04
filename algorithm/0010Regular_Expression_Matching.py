class Solution:
    def match(self, s, i, p, j):
        s_len, p_len = len(s), len(p)

        if i == s_len and j == p_len:
            return True

        if not (i < s_len and j < p_len):
            # corner 'a'-> 'ab*'
            if i == s_len and (p_len-j) % 2 == 0:
                for pos in range(j+1, p_len, 2):
                    if p[pos] != '*':
                        return False
                return True
            return False

        if p[j] != '*':
            if j+1 == p_len or p[j+1] != '*':
                if p[j] == '.':
                    return self.match(s, i+1, p, j+1)
                elif p[j] == s[i]:
                    return self.match(s, i+1, p, j+1)
                else:
                    return False
            else:
                return self.match(s, i, p, j+1)
        else:
            flag = False
            for pos in range(s_len-i+1):
                if p[j-1] == '.' or p[j-1]*pos == s[i:i+pos]:
                    flag = self.match(s, i+pos, p, j+1)
                    if flag:
                        return True
        return False

    def isMatch(self, s, p):
        """
        思路１:
        硬解
        超时
        思路2:
        递归
        :type s: str
        :type p: str
        :rtype: bool
        """

        return self.match(s, 0, p, 0)

    def isMatch2(self, s, p):
        if not s and not p:
            return True
        if len(p) >= 2 and p[1] == '*':
            if self.isMatch2(s, p[2:]):
                return True
            if p[0] == '.':
                return len(s) > 0 and self.isMatch2(s[1:], p)
            else:
                return len(s) > 0 and s[0] == p[0] and self.isMatch2(s[1:], p)
        else:
            if len(p) > 0:
                if p[0] == '.':
                    return len(s) > 0 and self.isMatch2(s[1:], p[1:])
                else:
                    return len(s) > 0 and s[0] == p[0] and self.isMatch2(s[1:], p[1:])
        return False

    def isMatch3(self, s, p):
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch3(s, p[2:]) or (first_match and self.isMatch3(s[1:], p))
        else:
            return first_match and self.isMatch3(s[1:], p[1:])

    def isMatch4(self, s, p):
        """
        :param s:
        :param p:
        :return:
        """
        s_len, p_len = len(s), len(p)
        dp = [[False]*(p_len+1) for _ in range(s_len+1)]
        dp[0][0] = True
        for i in range(s_len+1):
            for j in range(1, p_len+1):
                if p[j-1] == '*':
                    dp[i][j] = j > 1 and dp[i][j-2] or (i > 0 and dp[i-1][j] and p[j-2] in {'.', s[i-1]})
                else:
                    dp[i][j] = dp[i-1][j-1] and (i > 0 and p[j-1] in {'.', s[i-1]})
        return dp[s_len][p_len]


if __name__ == '__main__':
    s = Solution()
    t, p = "aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"
    print(s.isMatch4(t, p))