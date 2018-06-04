class Solution:
    def isPalindrome(self, x):
        """
        思路１:
        对数逆向后
        比较和原数的大小关系
        相等即代表为回文序列，但这样可能会溢出
        思路2:
        只逆向数的一半,和另一半比较如果相等即满足
        回文条件，逆向一半的临界点在新数刚刚大于等于原数
        时间复杂度为O(log10n)
        空间复杂度为O(1)
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x >= (1 << 31):
            return False

        old_num, rv_num = x, 0
        while x != 0:
            rv_num = rv_num*10 + x % 10
            x = x // 10

        if old_num == rv_num:
            return True
        return False

    def isPalindrome2(self, x):
        if x < 0 or ((x % 10 == 0) and (x != 0)):
            return False

        new = 0
        while True:
            new = new*10 + x % 10
            x = x // 10
            if x == new or new//10 == x:
                return True
            if x < new:
                return False

        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome2(353))
    print(s.isPalindrome2(10))
