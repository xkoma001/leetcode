class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ops = {'+', '-', '*', '/'}

        for ch in tokens:
            if ch in ops:
                second = stack.pop()
                first = stack.pop()
                if ch == '+':
                    stack.append(first+second)
                elif ch == '-':
                    stack.append(first-second)
                elif ch == '*':
                    stack.append(first*second)
                elif ch == '/':
                    if first * second < 0:
                        import math
                        rel = math.ceil(first/second)
                    else:
                        rel = first//second
                    stack.append(rel)
            else:
                stack.append(int(ch))
        return stack[0]

if __name__ == '__main__':
    s = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(s.evalRPN(tokens))
