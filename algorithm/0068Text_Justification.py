class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        i, m_len = 0, len(words)
        ans = []
        dp = [[0]*m_len for _ in range(m_len)]

        for i in range(m_len):
            for j in range(i, m_len):
                if i != j:
                    dp[i][j] = dp[i][j-1] + len(words[j])
                else:
                    dp[i][j] = len(words[i])
        i = 0
        while i < m_len:
            remain = m_len - i
            if dp[i][m_len-1]+remain-1 <= maxWidth:
                cur = words[i]
                for k in range(i+1, m_len):
                    cur += ' ' + words[k]
                cur += (maxWidth-dp[i][m_len-1]-remain+1)*' '
                ans.append(cur)
                break
            else:
                k = 0
                for j in range(m_len-1, i-1, -1):
                    wd_num = j-i+1
                    if dp[i][j]+wd_num-1 > maxWidth:
                        continue
                    else:
                        n = maxWidth-dp[i][j]
                        if wd_num == 1:
                            k = n
                            break
                        d, v = n // (wd_num-1), n % (wd_num-1)
                        if v == 0:
                            k = d
                            break
                        elif (wd_num-2)*(d+1)+1 > n:
                            continue
                        else:
                            k = d+1
                            break
                cur = words[i]
                for f in range(i+1, j):
                    cur += ' '*k + words[f]
                if wd_num > 1:
                    left_pad = maxWidth-(wd_num-2)*k-dp[i][j]
                    cur += ' '*left_pad+words[j]
                else:
                    cur += ' '*k
                ans.append(cur)
                i = j+1
        return ans

    def fullJustify2(self, words, maxWidth):
        ans, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(cur) + len(w) > maxWidth:
                for i in range(maxWidth-num_of_letters):
                    cur[i%(len(cur)-1 or 1)] += ' '
                ans.append(''.join(cur))
                cur = []
                num_of_letters = 0
            num_of_letters += len(w)
            cur.append(w)
        return ans + [' '.join(cur).ljust(maxWidth)]
