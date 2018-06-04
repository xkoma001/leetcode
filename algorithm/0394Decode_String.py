class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if ch == ']':
                cur = ""
                while stack[-1] != '[':
                    cur = stack.pop() + cur
                stack.pop()  # '['
                ntimes = ""
                while stack and stack[-1].isdigit():
                    ntimes = stack.pop() + ntimes
                cur = int(ntimes) * cur
                stack.append(cur)
            else:
                stack.append(ch)
        return ''.join(stack)
