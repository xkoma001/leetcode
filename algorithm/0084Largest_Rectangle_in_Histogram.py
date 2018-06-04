class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        m_len = len(heights)
        max_area = 0
        dp = [[0] * m_len for _ in range(m_len)]

        for i in range(m_len):
            for j in range(i, m_len):
                if i == j:
                    dp[i][j] = heights[j]
                else:
                    dp[i][j] = min(dp[i][j-1], heights[j])
                max_area = max(max_area, dp[i][j]*(j-i+1))

        return max_area

    def largestRectangleArea2(self, heights):
        heights = heights + [0]

        ans, stack = 0, []
        for i in range(len(heights)):
            while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                s = stack.pop()
                width = i-stack[-1]-1 if len(stack) > 0 else i
                ans = max(ans, width*heights[s])
            stack.append(i)
        return ans
