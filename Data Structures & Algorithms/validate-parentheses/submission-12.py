class Solution:
    def isValid(self, s: str) -> bool:
        # track close to open keys        
        keyMap = {"}": "{", "]": "[", ")": "("}
        stack = []

        for c in s:
            if c not in keyMap:
                stack.append(c)
            elif c in keyMap:
                # if char in map and valid match
                if stack and stack[-1] == keyMap[c]:
                    # remove char from stack
                    stack.pop()
                else:
                    return False

        # stack will be empty if valid parantheses
        return True if not stack else False
        