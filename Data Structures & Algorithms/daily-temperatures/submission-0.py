class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            # while stack not empty and temp > top of stack
            while stack and temp > stack[-1][0]:
                # pop top element of stack
                stack_temp, stack_index = stack.pop()

                # compute num days passed and update result
                res[stack_index] = i - stack_index

            # use stack to store (temp, index) pairs
            stack.append((temp, i))

        return res

        