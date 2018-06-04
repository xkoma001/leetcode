__author__ = 'xkoma'


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        cur_str = str.strip()
        if not cur_str:
            return 0
        sign = -1 if cur_str[0] == '-' else 1
        cur_str = cur_str[1:] if cur_str[0] in {'-', '+'} else cur_str

        last_num = -2
        for pos, ch in enumerate(cur_str):
            if ch not in nums:
                last_num = pos-1
                break
        if last_num != -2:
            cur_str = cur_str[:last_num+1]
        if not cur_str:
            return 0
        ans = sign*int(cur_str)
        int_max = (1 << 31) - 1
        int_min = -1 << 31
        ans = int_max if ans > int_max else ans
        ans = int_min if ans < int_min else ans
        return ans

if __name__ == '__main__':
    s = Solution()
    str = "-2147483648"
    print(s.myAtoi(str))
