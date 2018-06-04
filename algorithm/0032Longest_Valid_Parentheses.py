class Solution:
    def is_pair(self, s):
        stack = [(0, s[0])]
        for ch in s[1:]:
            if ch == ')':
                cur = stack.pop()
                if cur[0] == 0:
                    return True
            else:
                stack.append(ch)
        return False

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len, stack = 0, []
        pair = 0
        for i, ch in enumerate(s):
            if ch == ')':
                if not stack:
                    max_len = max(max_len, pair)
                    pair = 0
                else:
                    stack.pop()
                    pair += 2
            else:
                if not self.is_pair(s[i:]):
                    max_len = max(max_len, pair)
                    pair = 0
                stack.append('(')
        max_len = max(max_len, pair)
        return max_len

    def longestValidParentheses2(self, s):
        longest, stack = 0, []
        n = len(s)

        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)

        if not stack:
            return n

        b = n
        while stack:
            cur = stack.pop()
            longest = max(b-cur-1, longest)
            b = cur
        longest = max(b, longest)
        return longest

    def longestValidParentheses3(self, s):
        n = len(s)
        dp = [0] * n
        longest = 0
        for i in range(n):
            if s[i] == '(':
                dp[i] = 0
            else:
                if i >= 1 and s[i-1] == '(':
                    dp[i] = 2+dp[i-2] if i >= 2 else 2
                    longest = max(dp[i], longest)
                elif i >= 1 and s[i-1] == ')' and i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1]+2
                    dp[i] += dp[i-dp[i-1]-2] if i-dp[i-1]-2 >= 0 else 0
                    longest = max(dp[i], longest)
                else:
                    pass
        return longest
