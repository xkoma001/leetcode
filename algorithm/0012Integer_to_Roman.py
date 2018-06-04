class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = [0, 0, 1, 5, 10, 50, 100, 500, 1000]
        romans = ['', '', 'I', 'V', 'X', 'L', 'C', 'D', 'M']
        minus = ['I', 'X', 'C']
        rv = ""
        pos = 8
        while num != 0:
            count = num // roman[pos]
            num = num % roman[pos]
            if count != 0:
                rv += romans[pos]*count

            if romans[pos-1] in minus and roman[pos]-roman[pos-1] <= num:
                rv += romans[pos-1]+romans[pos]
                num -= roman[pos]-roman[pos-1]
            elif romans[pos-2] in minus and roman[pos]-roman[pos-2] <= num:
                rv += romans[pos-2] + romans[pos]
                num -= roman[pos]-roman[pos-2]
            pos -= 1
        return rv

if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(19))
