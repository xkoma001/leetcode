__author__ = 'xkoma'


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle:
            return 0
        h_len, n_len = len(haystack), len(needle)
        for i in range(h_len):
            if haystack[i: i+n_len] == needle:
                return i
        return -1

if __name__ == '__main__':
    pass