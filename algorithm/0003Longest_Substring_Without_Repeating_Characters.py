class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        思路：滑动窗口
        字符串ｓ，从0往后移动到索引ｋ没有重复，当前字符串cur_str长度为[0, k],
        移动到索引k+1时，与前面的字符串(索引m处)有字符重复,则新的当前字符串从[m+1, k+1]开始继续移动
        ,之前的最大无重复字符串长度为[0, k],如此循环，直到字符串结束．
        当前字符串可以用hash表(key,value)来表示,key表示字符值value表示索引值.
        时间开销为O(n),空间开销为T(n)
        :type s: str
        :rtype: str
        """
        if not s:
            return 0
        max_len, start, end, slide = 0, 0, 0, dict()
        for pos, ch in enumerate(s):
            if ch not in slide or slide[ch] < start:
                slide[ch] = pos
            else:
                cur_len = end - start+1
                max_len = cur_len if cur_len > max_len else max_len
                start = slide[ch] + 1
                slide[ch] = pos
            end = pos

        cur_len = end - start+1
        max_len = cur_len if cur_len > max_len else max_len  # 也有可能没有重复字符串
        return max_len

if __name__ == '__main__':
    s = Solution()
    str = "aub"
    print(s.lengthOfLongestSubstring(str))


