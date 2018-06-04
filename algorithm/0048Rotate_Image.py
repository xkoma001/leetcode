class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m_len = len(matrix)
        # reverse
        for i in range(m_len//2):
            matrix[i], matrix[m_len-1-i] = matrix[m_len-1-i], matrix[i]
        # duichen
        for i in range(m_len):
            for j in range(i+1, m_len):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return
