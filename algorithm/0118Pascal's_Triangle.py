class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []

        cur_len = 1
        for i in range(numRows):
            cur_rel = []
            for j in range(cur_len):
                if j == 0 or j == cur_len-1:
                    cur_rel.append(1)
                else:
                    cur_rel.append(ans[i-1][j-1]+ans[i-1][j])
            ans.append(cur_rel)
            cur_len += 1
        return ans
