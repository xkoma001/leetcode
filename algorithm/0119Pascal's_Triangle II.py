class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        ans = [1]
        for i in range(1, rowIndex):
            ans = list(map(lambda x, y: x+y, [0]+ans, ans+[0]))
        return ans

    def getRow2(self, rowIndex):
        ans = [0] * (rowIndex+1)
        ans[0] = 1

        for i in range(1, rowIndex+1):
            for j in range(i, 0, -1):
                ans[j] += ans[j-1]
        return ans
