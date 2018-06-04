class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])

        low, high = 0, n-1
        while low < high:
            mid = (low+high)//2
            if matrix[0][mid] == target:
                return True
            elif matrix[0][mid] < target:
                low = mid+1
            else:
                high = mid

        if matrix[0][high] < target:
            pass
        elif matrix[0][high] > target and high == 0:
            return False
        elif matrix[0][high] > target:
            high -= 1

        for col in range(high, -1, -1):
            low, high = 0, m-1
            while low <= high:
                mid = (low+high)//2
                if matrix[mid][col] == target:
                    return True
                elif matrix[mid][col] < target:
                    low = mid+1
                else:
                    high = mid-1
        return False

    def searchMatrix2(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])

        i, j = 0, n-1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False
