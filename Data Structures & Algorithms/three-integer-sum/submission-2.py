class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        # sort array to handle duplicates
        nums.sort()

        for i, a in enumerate(nums):
            # break since all remaining numbers are positive
            if a > 0:
                break

            # skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # set 2 pointers
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                threesum = a + nums[l] + nums[r]

                # if 3some > 0, decrease num
                if threesum > 0: 
                    r -= 1
                # if 3some < 0, increase num
                if threesum < 0: 
                    l += 1
                if threesum == 0: 
                    res.append([a, nums[l], nums[r]])
                    
                    l += 1
                    r -= 1

                    # skip duplicates at left pointer
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
        



        
        