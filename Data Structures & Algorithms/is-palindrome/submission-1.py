class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create new string
        new_s = ""

        # loop thru s
        for c in s:
            # if c is alpha numeric
            if c.isalnum():
                # append to new string
                new_s += c.lower()

        # check if new string = new string in reverse
        return new_s == new_s[::-1]
        # [start:stop:step]
       
        