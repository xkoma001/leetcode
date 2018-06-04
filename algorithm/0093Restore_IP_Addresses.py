class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []

        def ip_combine(s, i, rel):
            if i == 4 and not s:
                ans.append(rel[:-1])
                return

            if not (i < 4 and s):
                return

            tmp = rel
            for j in range(3):
                rel = tmp
                if j == 0 or (s[0] != '0' and (len(s) > j and int(s[:j+1]) <= 255)):
                    rel = rel + s[:j+1] + '.'
                    ip_combine(s[j+1:], i+1, rel)
            return
        ip_combine(s, 0, "")
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses("0000"))
