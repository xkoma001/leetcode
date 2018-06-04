class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack = []
        matchs = {'(': ')', '{': '}', '[': ']'}
        for ch in s:
            if ch in matchs:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                elif matchs[stack[-1]] != ch:
                    return False
                else:
                    stack.pop()

        if len(stack) != 0:
            return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isValid("[{()}]"))