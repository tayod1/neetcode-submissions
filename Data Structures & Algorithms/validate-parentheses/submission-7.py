class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return False

        input = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if c in input:
                if stack and stack[-1] == input.get(c):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return stack == []



        