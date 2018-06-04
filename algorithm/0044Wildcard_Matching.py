class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        s_len, p_len = len(s), len(p)

        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == s_len and j == p_len:
                memo[(i, j)] = True
                return memo[(i, j)]
            if j < p_len:
                if p[j] == '*':
                    memo[(i, j)] = helper(i, j+1) or (i < s_len and helper(i+1, j))
                else:
                    memo[(i, j)] = i < s_len and p[j] in {s[i], '?'} and helper(i+1, j+1)
            memo[(i, j)] = False
            return memo[(i, j)]
        helper(0, 0)
        return memo[(s_len, p_len)] if (s_len, p_len) in memo else False

    def isMatch2(self, s, p):
        s_len, p_len = len(s), len(p)
        i, j = 0, 0
        star_index = -1

        while i < s_len:
            if j < p_len and p[j] in {s[i], '?'}:
                i += 1
                j += 1
            elif j < p_len and p[j] == '*':
                star_index = j
                j += 1
                match = i
            elif star_index != -1:
                match += 1
                i = match
                j = star_index + 1
            else:
                return False
        while j < p_len and p[j] == '*':
            j += 1
        return j == p_len
