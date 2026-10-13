class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        store_map = {}

        while i <= len(nums):
            diff = target - nums[i]
            if diff in store_map:
                return [store_map[diff], i]
            else:
                store_map[nums[i]] = i
                i = i + 1

        