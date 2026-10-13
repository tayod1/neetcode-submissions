class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        # init 2 pointers
        l, r = 0, len(heights) - 1

        while l < r:
            # compute the area as height x width
            area = min(heights[l], heights[r]) * (r - l)

            # update res with max area
            res = max(res, area)
            
            # move the shorter pointer first
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return res


            
        