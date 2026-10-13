class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums) # for O(1) lookup

        for n in nums:
            # start of sequence
            if n - 1 not in nums: 
                # track curr length
                curr_length = 1
                
                # use curr length to increment n
                while n + curr_length in nums:
                    curr_length += 1

                # update longest
                longest = max(longest, curr_length)

        return longest

        