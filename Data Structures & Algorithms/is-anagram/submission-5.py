class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # strings must be equal length to be anagrams
        if len(s) != len(t): return False
        
        # use a set to store all unique chars
        chars = set(s)
        
        # loop thru chars set
        for c in chars:
            # check count of char matches in each string
            if s.count(c) != t.count(c):
                return False

        return True
        