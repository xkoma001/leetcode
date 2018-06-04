class Solution:
    def fac(self, x, n):
        """
        n > 0
        :param x:
        :param n:
        :return:
        """
        if n == 0:
            return 1
        if n == 1:
            return x

        m = n // 2
        left = n - m*2
        rv = self.fac(x, m)
        rv *= rv
        return rv * self.fac(x, left)

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        思路1:
            return x**3
            时间复杂度为O(n)
            无聊水题，以后看解答也许有其他深意
            超时考虑降幂
        思路2:
        n可以想办法折半的
        eg: 5 ** 6 = 5 ** 3 * 2
        时间复杂度为O(logn)
        思路3:
        迭代法
        把十进制数ｎ看成二进制表示位从低到高(00010001)
        新的乘积是前一次乘积的２倍
        """
        neg, rv = False, float(1)
        if n == 0:
            return float(1)
        if n < 0:
            neg = True
            n = -n

        rv *= self.fac(x, n)
        if neg:
            rv = float(1) / rv
        return rv

    def myPow2(self, x, n):
        rv = 1.0
        if n < 0:
            n = -n
            x = 1/x

        current_product = x
        while n != 0:
            if (n % 2) == 1:
                rv *= current_product
            n = n // 2
            current_product *= current_product

        return rv

if __name__ == '__main__':
    s = Solution()
    x, n = 3, 7
    print(s.myPow(x, n))
    print(s.myPow2(x, n))
