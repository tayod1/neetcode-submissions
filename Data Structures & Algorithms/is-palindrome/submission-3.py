class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # move l forward until it points to an alphanumeric character
            while l < r and not s[l].isalnum():
                l += 1
            # move r backward until it points to an alphanumeric character
            while r > l and not s[r].isalnum():
                r -= 1
            # if the lowercase characters at l and r don't match, return false
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1

        # if the loop finishes without mismatches, return true.
        return True
       
        