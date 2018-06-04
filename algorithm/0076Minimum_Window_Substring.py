class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        start, end, s_len = 0, 0, len(s)
        t_len, m = len(t), dict()
        from collections import defaultdict
        m = defaultdict(int)
        min_str = None

        for c in t:
            m[c] += 1

        while end < s_len:
            if m[s[end]] > 0:
                t_len -= 1

            m[s[end]] -= 1
            end += 1

            while t_len == 0 and start < end:
                if not min_str:
                    min_str = s[start:end]
                elif end-start < len(min_str):
                    min_str = s[start:end]

                m[s[start]] += 1
                if m[s[start]] > 0:
                    t_len += 1
                start += 1

        return min_str if min_str else ""
