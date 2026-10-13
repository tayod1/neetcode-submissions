class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setty = set()

        for n in nums:
            if n in setty:
                return True
            setty.add(n)
            
        return False
         