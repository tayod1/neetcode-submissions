class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

        # Time complexity: O(n) 
            # - visits all n items to build the set
            
        # Space complexity: O(n)
            # Extra space - set can hold up to n items