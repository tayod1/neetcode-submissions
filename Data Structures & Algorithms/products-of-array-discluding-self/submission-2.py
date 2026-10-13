class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        non_zero_product = 1
        num_zero = 0

        for n in nums:
            if n!= 0:
                non_zero_product *= n
            else:
                num_zero += 1

        if num_zero > 1:
            return [0] * len(nums)

        res = [0] * len(nums)
        for i in range(len(nums)):
            if num_zero:
                res[i] = 0 if nums[i] else non_zero_product
            else:
                res[i] = non_zero_product // nums[i]

        return res
        