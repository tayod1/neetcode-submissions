class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        # store all unique characters
        set_s = set(s)
        
        # for each unique char track:
            # 1. how many chars in s match it
            # 2. how many k replacements are needed
        
        for c in set_s:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    # increment when chars match
                    count += 1

                # while the window needs more than k replacements
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        # decrement num of matching chars
                        count -= 1
                    # shrink window from left
                    l += 1

                # update max substring length
                res = max(res, r - l + 1)
        return res

        