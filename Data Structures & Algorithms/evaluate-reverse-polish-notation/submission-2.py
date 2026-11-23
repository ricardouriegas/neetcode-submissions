class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            stack.append(i)
            if i == "+":
                stack.pop()
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                stack.append(op1 + op2)
            elif i == "-":
                stack.pop()
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(op1 - op2)
            elif i == "*":
                stack.pop()
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                stack.append(op1 * op2)
            elif i == "/":
                stack.pop()
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(op1 / op2)

        return int(stack.pop())

