class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        m_len = len(triangle)
        paths = [0] * m_len
        cur_min = paths[0] = triangle[0][0]

        for i in range(1, m_len):
            if i == m_len-1:
                cur_min = paths[0] + triangle[i][0]
            for j in range(i, -1, -1):
                if j == i:
                    paths[j] = triangle[i][j] + paths[j-1]
                elif j == 0:
                    paths[j] = triangle[i][j] + paths[j]
                else:
                    paths[j] = triangle[i][j] + min(paths[j], paths[j-1])
                if i == m_len-1:
                    cur_min = min(cur_min, paths[j])
        return cur_min

    def minimumTotal2(self, triangle):
        if not triangle:
            return
        row = len(triangle)
        paths = [val for val in triangle[row-1]]

        for i in range(row-2, -1, -1):
            for j in range(i+1):
                paths[j] = min(paths[j], paths[j+1]) + triangle[i][j]
        return paths[0]

if __name__ == '__main__':
    s = Solution()
    trigle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print(s.minimumTotal(trigle))
