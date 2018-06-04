class Solution:
    table = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def search_digits(self, digits, rv, cur_str):
        if not digits:
            return []
        for ch in self.table[int(digits[0])]:
            new_str = cur_str + ch
            if len(digits) != 1:
                self.search_digits(digits[1:], rv, new_str)
            else:
                rv.append(new_str)

    def letterCombinations(self, digits):
        """
        思路１：
        只想到暴力方法,全局搜索遍历
        搜索类似于dfs
        O(3^n)
        思路2:
        迭代方法，类似于bfs
        :type digits: str
        :rtype: List[str]
        """
        rv = []
        self.search_digits(digits, rv, "")
        return rv

    def letterCombinations2(self, digits):
        if not digits:
            return []
        from functools import reduce
        letters = [int(letter) for letter in digits]
        return reduce(lambda acc, digit: [x+ch for x in acc for ch in self.table[digit]], letters, [""])

if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))
    print(s.letterCombinations2('23'))
