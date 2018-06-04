class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []

        rv = [["", (n, n)]]  # 左边代表'('剩余个数, 右边代表')'剩余个数

        step = 0
        while step < 2*n:
            step += 1
            for cur_st in rv[:]:
                left_l, left_r = cur_st[1][0], cur_st[1][1]
                if left_l > 0:
                    rv.append([cur_st[0]+'(', (left_l-1, left_r)])
                if left_r > left_l:
                    rv.append([cur_st[0]+')', (left_l, left_r-1)])
                rv.remove(cur_st)
        return [cur_st[0] for cur_st in rv]

if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
