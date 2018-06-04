class Solution:
    start, max_len, m_len = 0, 1, 0

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        思路１:
        每新增一个字符，以该字符为结尾的回文有以下几种情况
        1. 前一个字符是回文序列(前一个字符任意一种回文，都会对当前字符造成影响)，eg: aba, acbbca, ccacca
        2. 与前一个字符构成回文(eg: bb, cc)
        3. 自身作为回文 eg: a
        构建一个列表l,列表索引代表字符位置(end)，索引对应的列表值为以该字符结尾的回文序列的起点start位置(所有的).
        默认值为(l[end]=[end])该字符本身
        时间复杂度：
         O(n2) 时间不稳定，思考不够抽象,有重复计算,越往后计算量越大
         超时了
        思路2:
        动态规划
        o(n2)
        思路3:
        从中心扩散，总共2n-1个center,
        每个center有n次比较，时间开销为O(n2)
        """

        if not s:
            return ''

        l, rv = [[0]], [0, 0]
        cur_max = 1

        for pos in range(1, len(s)):
            l.append([])
            # 1
            for index in l[pos-1]:
                if index >= 1 and s[index-1] == s[pos]:
                    l[pos].append(index-1)
                    if (pos-index+2) > cur_max:
                        cur_max = pos-index+2
                        rv = [index-1, pos]

            # 2
            if s[pos] == s[pos-1]:
                l[pos].append(pos-1)
                if 2 > cur_max:
                    cur_max = 2
                    rv = [pos-1, pos]
            # 3
            l[pos].append(pos)

        return s[rv[0]:rv[1]+1]

    def longestPalindrome2(self, s):
        """
        P(i,j) = if (s[i] == s[j], P(i+1, j-1)) true else false
        初始P(i,i) = true
        P(i, i+1) if s[i] == s[i+1])
        也超时了尴尬，主要创建这个表太花时间
        :param s:
        :return:
        """

        max_len, m_len = 1, len(s)
        start = 0
        dp = [[0 for _ in range(m_len)] for _ in range(m_len)]

        for i in range(m_len-1, -1, -1):
            for j in range(i, m_len):
                if s[i] == s[j] and (j-i < 3 or dp[i+1][j-1] == 1):
                    dp[i][j] = 1
                    if j-i+1 > max_len:
                        max_len = j-i+1
                        start = i
        return s[start:start+max_len]

    def longestPalindrome3(self, s):
        if not s:
            return s

        self.m_len = len(s)
        for pos, ch in enumerate(s):
            self.expand_center(s, pos, pos)
            if pos < self.m_len-1:
                self.expand_center(s, pos, pos+1)

        return s[self.start:self.start+self.max_len]

    def expand_center(self, s, i, j):
        while i >= 0 and j < self.m_len and s[i] == s[j]:
            i -= 1
            j += 1

        if j-i-1 > self.max_len:
            self.max_len = j-i-1
            self.start = i+1
        return

if __name__ == '__main__':
    s = Solution()
    str = "babad"
    str2 = "klvxwqyzugrdoaccdafdfrvxiowkcuedfhoixzipxrkzbvpusslsgfjocvidnpsnkqdfnnzzawzsslwnvvjyoignsfbxkgrokzyusxikxumrxlzzrnbtrixxfioormoyyejashrowjqqzifacecvoruwkuessttlexvdptuvodoavsjaepvrfvbdhumtuvxufzzyowiswokioyjtzzmevttheeyjqcldllxvjraeyflthntsmipaoyjixygbtbvbnnrmlwwkeikhnnmlfspjgmcxwbjyhomfjdcnogqjviggklplpznfwjydkxzjkoskvqvnxfzdrsmooyciwulvtlmvnjbbmffureoilszlonibbcwfsjzguxqrjwypwrskhrttvnqoqisdfuifqnabzbvyzgbxfvmcomneykfmycevnrcsyqclamfxskmsxreptpxqxqidvjbuduktnwwoztvkuebfdigmjqfuolqzvjincchlmbrxpqgguwuyhrdtwqkdlqidlxzqktgzktihvlwsbysjeykiwokyqaskjjngovbagspyspeghutyoeahhgynzsyaszlirmlekpboywqdliumihwnsnwjc"
    print(s.longestPalindrome(str))
    print(s.longestPalindrome2(str2))
    print(s.longestPalindrome3(str2))
