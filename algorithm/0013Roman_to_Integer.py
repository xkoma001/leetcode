class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                       'M': 1000}
        rv, s_len = 0, len(s)

        for pos in range(s_len):
            if pos < s_len-1 and romans[s[pos]] < romans[s[pos+1]]:
                rv -= romans[s[pos]]
            else:
                rv += romans[s[pos]]
        return rv

