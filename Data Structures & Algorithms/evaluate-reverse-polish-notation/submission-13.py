class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            # 1. pop 2 most recent numbers
            # 2. apply operations then add back to stack
            
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                print(stack, c)
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                # if c is a num, push it onto stack
                stack.append(int(c))

        # after processing all tokens, the stack only contains one value 
        return stack[0]
        