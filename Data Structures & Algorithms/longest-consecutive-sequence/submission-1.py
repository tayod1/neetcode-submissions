class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums) # for O(1) lookup

        for n in nums:
            if n - 1 not in nums: # start of sequence
                curr_length = 1
                while n + curr_length in nums:
                    curr_length += 1

                longest = max(longest, curr_length)

        return longest

        