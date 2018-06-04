class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = 0
        s = s.strip()
        for ch in s[::-1]:
            if ch == ' ':
                break
            m += 1
        return m

    def lengthOfLastWord2(self, s):
        a = s.split()
        if not a:
            return 0
        return len(a[-1])
