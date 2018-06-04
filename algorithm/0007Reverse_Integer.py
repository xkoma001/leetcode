class Solution:
    def reverse(self, x):
        """
        思路１：
        一直考虑位运算，思维陷入死胡同了，用原来的做法就可以了，本人对这种数的操作极不擅长
        思路2:
        不断的相除，得到相反的结果
        假设数的位数为n
        则时间开销为O(n)
        思路3:
        转换数字成字符串
        :type x: int
        :rtype: int
        """
        rv = 0
        sign = -1 if x < 0 else 1
        x *= sign
        while x != 0:
            tail = x % 10
            rv = rv * 10 + tail
            x = x // 10
        return sign*rv*(rv <= (1 << 31) -1)

    def reverse2(self, x):
        sign = -1 if x < 0 else 1
        x *= sign
        rv = int(str(x)[::-1])
        return sign*rv*(rv <= (1 << 31) -1)

if __name__ == '__main__':
    s = Solution()
    x = 123
    print(s.reverse(x))
