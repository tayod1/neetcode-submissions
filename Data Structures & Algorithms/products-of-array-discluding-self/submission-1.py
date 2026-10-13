class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        output = [0] * len(nums)

        for i in range(len(nums)):
            res_val = 1

            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    res_val *= nums[j]

            output[i] = res_val

        return output
        