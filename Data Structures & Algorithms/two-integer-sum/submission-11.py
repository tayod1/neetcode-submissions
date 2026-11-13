class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for i, n in enumerate(nums):
            calc = target - n
            if calc in store:
                return [store[calc], i]
            store[n] = i

        # Time complexity: O(n)
            # 1 loop through at most n items

        # Space complexity: O(n)
            # as n grows, size of the set grows