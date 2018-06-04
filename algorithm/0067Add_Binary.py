class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m, n = len(a)-1, len(b)-1

        if m < n:
            m, n = n, m
            a, b = b, a
        carry = 0
        ans = ""
        while m >= 0 and n >= 0:
            cur = int(a[m]) + int(b[n]) + carry
            ans = str(cur % 2) + ans
            carry = cur // 2
            m -= 1
            n -= 1

        for pos in range(m, -1, -1):
            cur = int(a[pos]) + carry
            ans = str(cur % 2) + ans
            carry = cur // 2
        if carry != 0:
            ans = str(carry) + ans
        return ans

if __name__ == '__main__':
    s = Solution()
    a, b = "1", "111"
    print(s.addBinary(a, b))