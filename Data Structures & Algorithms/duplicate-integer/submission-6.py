class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # compare set(nums) to nums 
        # since a set contains only unique items
        
        return len(set(nums)) < len(nums)