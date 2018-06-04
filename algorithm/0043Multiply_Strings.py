class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1_len, num2_len = len(num1), len(num2)
        multi_len = num1_len + num2_len
        multi = ['0'] * multi_len

        for i in range(num1_len-1, -1, -1):
            for j in range(num2_len-1, -1, -1):
                rv = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))

                high, cur_pos = rv + ord(multi[i+j+1])-ord('0'), i+j
                multi[i+j+1] = chr(high % 10 + ord('0'))
                while high // 10 != 0 and cur_pos >= 0:
                    high = high // 10 + ord(multi[cur_pos]) - ord('0')
                    multi[cur_pos] = chr(high % 10 + ord('0'))
                    cur_pos -= 1

        find = False
        for i in range(multi_len):
            if multi[i] != '0':
                find = True
                multi = multi[i:]
                break
        if not find:
            multi = ['0']

        return ''.join(multi)

    def multiply2(self, num1, num2):
        m, n = len(num1), len(num2)
        multi = [0] * (m+n)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                multi[i+j+1] += mul
                multi[i+j] += multi[i+j+1] // 10
                multi[i+j+1] %= 10

        index = 0
        while len(multi) > 1 and (index < m+n-1) and multi[index] == 0:
            index += 1
        multi = multi[index:]
        return ''.join(map(str, multi))


if __name__ == '__main__':
    s = Solution()
    print(s.multiply2('1', '1'))

