class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        tracking = {}

        # loop using enumerate to track index & num
        for i, n in enumerate(numbers):
            # compute diff using target
            diff = target - n

            # if diff in tracking and 1-index is unique
            if diff in tracking and tracking[diff] != i + 1:
                # return sorted result (in increasing order)
                return sorted([i + 1, tracking[diff]])
            
            # update tracking map with 1-index of num
            tracking[n] = i + 1

        