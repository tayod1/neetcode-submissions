class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        # important to handle case where there are zeros
        non_zero_product = 1
        num_zero = 0

        for n in nums:
            if n!= 0:
                # get product of all numbers != 0
                non_zero_product *= n
            else:
                # count number of zeros
                num_zero += 1

        if num_zero > 1:
            # more than 1 zero guarantees all zeros in res
            return [0] * len(nums)

        res = [0] * len(nums)
        for i in range(len(nums)):
            # if 1 zero
            if num_zero:
                # res[i] = 0 if nums[i] != 0
                res[i] = 0 if nums[i] else non_zero_product
                # else res[i] = product of every num besides 0
                        # because res[i] = 0 in that case
            # if no zeros
            else:
                # res[i] = product of every num / nums[i]
                res[i] = non_zero_product // nums[i]

        return res
        