class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ans = []
        s_len, p_len = len(s), len(p)
        if not p_len:
            return []

        p_ana = [0] * 26
        s_ana = [0] * 26

        for ch in p:
            p_ana[ord(ch)-ord('a')] += 1

        for i in range(s_len):
            if i+p_len > s_len:
                break
            if i == 0:
                for j in range(i, i+p_len):
                    s_ana[ord(s[j])-ord('a')] += 1
            else:
                s_ana[ord(s[i-1])-ord('a')] -= 1
                s_ana[ord(s[i+p_len-1])-ord('a')] += 1
            if s_ana == p_ana:
                ans.append(i)
        return ans

    def findAnagrams2(self, s, p):
        if not s or not p:
            return []

        from collections import defaultdict
        ans = []
        ana = defaultdict(int)
        s_len, p_len = len(s), len(p)
        left = right = 0
        count = p_len

        for ch in p:
            ana[ch] += 1

        while right < s_len:
            if ana[s[right]] > 0:
                count -= 1

            ana[s[right]] -= 1
            right += 1

            if count == 0:
                ans.append(left)

            if right-left == p_len:
                if ana[s[left]] >= 0:
                    count += 1
                ana[s[left]] += 1
                left += 1
        return ans
