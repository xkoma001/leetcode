class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        max_int, min_int = 2147483647, -2147483648
        if not divisor:
            return max_int

        sign = 1 if (divisor >= 0 and dividend >= 0) or (divisor < 0 and dividend < 0) else -1
        dend, disor = abs(dividend), abs(divisor)

        ans = 0
        while dend >= disor:
            tmp, multiply = disor, 1
            while dend >= tmp:
                dend -= tmp
                ans += multiply
                tmp <<= 1
                multiply <<= 1
        ans *= sign
        if ans > max_int:
            return max_int
        return ans
