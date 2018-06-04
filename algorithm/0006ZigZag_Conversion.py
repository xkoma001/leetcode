class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # v
        if numRows < 1:
            return ""
        elif numRows == 1:
            return s

        ans, col = [], [0]*numRows
        j, step, m_len, row = -1, 0, len(s), 0

        import copy
        while step < m_len:
            ans.append(copy.deepcopy(col))
            j += 1
            if row == 0:
                for i in range(numRows):
                    if step == m_len:
                        break
                    ans[j][i] = s[step]
                    step += 1
                row = numRows-2
            else:
                ans[j][row] = s[step]
                step += 1
                row -= 1

        rel = ""
        for i in range(numRows):
            for k in range(j+1):
                if ans[k][i] != 0:
                    rel += ans[k][i]
        return rel

    def convert2(self, s, numRows):
        if numRows == 1 or len(s) <= numRows:
            return s

        l = [''] * numRows
        index, step = 0, 1
        for x in s:
            l[index] += x
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            index += step

        return ''.join(l)
