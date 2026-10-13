class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use hashmap to track nums and its index
        tracking = {}

        for i, n in enumerate(nums):
            # compute diff 
            diff = target - n
            
            # refer to hashmap for seen values / indices
            if diff in tracking and tracking[diff] != i:
                return [tracking[diff], i]

            # update hashmap
            tracking[n] = i


        