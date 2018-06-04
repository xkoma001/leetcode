class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        left, right, height = [0]*n, [n]*n, [0]*n
        max_area = 0

        for i in range(m):
            cur_left, cur_right = 0, n
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                    left[j] = max(left[j], cur_left)
                else:
                    height[j] = 0
                    cur_left = j+1
                    left[j] = 0
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    cur_right = j
                    right[j] = n
            for j in range(n):
                max_area = max(max_area, (right[j]-left[j])*height[j])
        return max_area

    def maximalRectangle2(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        row, col = len(matrix), len(matrix[0])
        h = [0] * (col+1)
        ans = 0
        for i in range(row):
            stack = []
            for j in range(col+1):
                if j < col:
                    if matrix[i][j] == '1':
                        h[j] += 1
                    else:
                        h[j] = 0
                while stack and h[stack[-1]] > h[j]:
                    s = stack.pop()
                    width = j-stack[-1]-1 if stack else j
                    ans = max(ans, width*h[s])
                stack.append(j)
        return ans
