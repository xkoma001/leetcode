class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        ans = []
        m_len, wd_count, wd_len = len(s), len(words), len(words[0])
        from collections import defaultdict
        target = defaultdict(int)

        for wd in words:
            target[wd] += 1

        for i in range(0, m_len-wd_count*wd_len+1):
            seen = defaultdict(int)
            j = 0
            while j < wd_count:
                wd = s[i+j*wd_len:i+j*wd_len+wd_len]
                if wd not in target:
                    break
                else:
                    seen[wd] += 1
                    if seen[wd] > target[wd]:
                        break
                j += 1
            if j == wd_count:
                ans.append(i)
        return ans

