class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m*n-1

        while low <= high:
            mid = (low + high) // 2
            mid_val = matrix[mid//n][mid % n]
            if mid_val == target:
                return True
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

