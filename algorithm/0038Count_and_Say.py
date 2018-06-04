class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ''

        m = 1
        new_str, cur_str = '', '1'
        while m < n:
            str_len, count = len(cur_str), 0
            for i in range(str_len):
                count += 1
                if i != str_len-1 and cur_str[i+1] != cur_str[i]:
                    new_str += str(count) + cur_str[i]
                    count = 0
            if count:
                new_str += str(count) + cur_str[str_len-1]
            cur_str, new_str = new_str, ''
            m += 1
        return cur_str


