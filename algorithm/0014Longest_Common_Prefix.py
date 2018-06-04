class Solution:
    def longestCommonPrefix(self, strs):
        """
        思路１：
         从第一个字符串的头，与后面的字符串一个字符一个字符的比较直到不相等，
         则得到最长公共头
         假设最长头为m,字符串数组大小为n
         则时间开销为O(mn)
        :type strs: List[str]
        :rtype: str
        """
        com_prefix, equal = '', True
        if not strs:
            return ''

        for pos, ch in enumerate(strs[0]):
            for s in strs[1:]:
                if (len(s) < (pos + 1)) or s[pos] != ch:
                    equal = False
                    break
            if equal:
                com_prefix += ch

        return com_prefix


if __name__ == '__main__':
    s = Solution()
    strs=['qwrwqsgalsdgalfs']
    print(s.longestCommonPrefix(strs))
