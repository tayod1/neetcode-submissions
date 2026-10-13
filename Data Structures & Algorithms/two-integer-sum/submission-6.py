class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracking = {}

        for i, n in enumerate(nums):
            tracking[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in tracking and tracking[diff] != i:
                return [i, tracking[diff]]

        return []
        