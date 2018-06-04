class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m_len = len(s)
        i, j = 0, m_len-1

        while i < j:
            while i < m_len and s[i].isalnum() is False:
                i += 1
            while j >= 0 and s[j].isalnum() is False:
                j -= 1
            if i < m_len and j >= 0 and s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
