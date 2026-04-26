class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        ops = ['+', '-', '*', '/']
        for i in tokens:
            print(i, s)
            if i in ops:
                x = int(s.pop())
                y = int(s.pop())
            if i == '+':
                s.append(x + y)
            elif i == '-':
                s.append(y - x)
            elif i == '*':
                s.append(x * y)
            elif i == '/':
                s.append(y / x)
            else:
                s.append(i)
            
        return int(s[0])