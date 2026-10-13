class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracking = {}
        # track indices which character appear

        l, res = 0, 0

        for r, c in enumerate(s):
            # if char already seen
            if c in tracking:
                # jump left pointer to one position             
                l = max(tracking[c] + 1, l)
                # after its previous occurrence

            # store the last index where each character appeared
            tracking[c] = r

            # update the longest length
            res = max(res, r - l + 1)

        return res
            

        