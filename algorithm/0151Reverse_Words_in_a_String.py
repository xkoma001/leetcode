class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s.strip()
        n, ans = len(s), []

        i, j = 0, 0
        while i < n:
            if s[i] == ' ':
                i += 1
            else:
                j = i
                while j < n and s[j] != ' ':
                    j += 1
                ans.append(s[i:j])
                i = j
        return ' '.join(ans[::-1])



