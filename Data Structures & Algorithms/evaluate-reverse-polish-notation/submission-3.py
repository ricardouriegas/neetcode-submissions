class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                stack.append(op1 + op2)
            elif i == "-":
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(op1 - op2)
            elif i == "*":
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                stack.append(op1 * op2)
            elif i == "/":
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(op1 / op2)
            else:
                stack.append(i)

        return int(stack.pop())

