class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for c in s:
            count_s[c] = count_s.get(c, 0) + 1
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        return count_s == count_t

        # Time complexity: O(n)
            # visits all n items to build the sets

        # Space complexity: O(1)
            # the sets store at most 26 entries,
            # they don't grow with n hence O(1)
        