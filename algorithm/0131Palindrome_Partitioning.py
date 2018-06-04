class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def is_palindrome(start, end):
            if start == end:
                return True
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def palin_partion(start, end):
            ans = []
            if start > end:
                return []
            if start == end:
                return [[s[start]]]

            for i in range(start, end+1):
                if is_palindrome(start, i):
                    if i == end:
                        ans.append([s[start:i+1]])
                        continue
                    sub = palin_partion(i+1, end)
                    if sub:
                        for cur in sub:
                            ans.append([s[start:i+1]]+cur)
            return ans

        s_len = len(s)
        return palin_partion(0, s_len-1)

    def partition2(self, s):
        ans = []

        def is_pair(s):
            return s == s[::-1]

        def dpth(s, path):
            if not s:
                ans.append(path[:])

            for j in range(len(s)):
                if is_pair(s[:j+1]):
                    path.append(s[:j+1])
                    dpth(s[j+1:], path)
                    path.pop()

            return

        dpth(s, [])
        return ans

    def partition3(self, s):
        m_len = len(s)
        pair = [[0] * m_len for _ in range(m_len)]
        paths = [[[]]]

        for i in range(m_len):
            paths.append([])
            j = i + 1
            for left in range(0, i+1):
                if s[left] == s[i] and (i-left <= 1 or pair[left+1][i-1]):
                    pair[left][i] = 1
                    for cur in paths[left]:
                        paths[j].append(cur+[s[left:i+1]])
        return paths[m_len]

if __name__ == '__main__':
    s = Solution()
    print(s.partition3("aab"))
