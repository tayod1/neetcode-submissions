class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        # pair each car's position with its speed
        pair = [(p, s) for p, s in zip(position, speed)]

        # reverse sort the cars - closest to target first
        pair.sort(reverse=True)

        for p, s in pair:
            # compute time to reach target
            time_to_reach = (target - p) / s

            # push time onto stack
            stack.append(time_to_reach)

            # if stack has more than 1 elem
            if len(stack) >= 2:
                # if new car's time is <= previous time
                if stack[-1] <= stack[-2]:
                    # remove - new car won't form new fleet
                    stack.pop()

        # num of remaining times in stack = num of fleets
        return len(stack)
    