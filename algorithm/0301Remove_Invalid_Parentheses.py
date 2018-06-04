class Solution:
    def removeInvalidParentheses(self, s):
        ans = []

        def remove(s, i_end, j_end, pair):
            count = 0
            for i in range(i_end, len(s)):
                if s[i] == pair[0]:
                    count += 1
                elif s[i] == pair[1]:
                    count -= 1
                if count >= 0:
                    continue
                for j in range(j_end, i+1):
                    if s[j] == pair[1] and (j == j_end or s[j-1] != pair[1]):
                        remove(s[:j]+s[j+1:], i, j, pair)
                return

            new_s = s[::-1]
            if pair[1] == ')':
                remove(new_s, 0, 0, (')', '('))
            else:
                ans.append(new_s)
            return
        remove(s, 0, 0, ('(', ')'))
        return ans

    def removeInvalidParentheses2(self, s):
        def is_valid(s):
            count = 0
            for ch in s:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        if not s:
            return [""]
        from collections import deque
        queue = deque()
        m_hash = dict()
        ans = []
        queue.append(s)

        find = False
        while queue:
            cur_s = queue.popleft()
            if is_valid(cur_s):
                find = True
                ans.append(cur_s)
            if find:
                continue

            for i in range(len(cur_s)):
                if cur_s[i] != '(' and cur_s[i] != ')':
                    continue
                new_s = cur_s[:i] + cur_s[i+1:]
                if new_s not in m_hash:
                    m_hash[new_s] = True
                    queue.append(new_s)
        return ans
