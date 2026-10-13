class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        window_size = len(s1)

        for l in range(len(s2)):
            r = l + window_size
            sub_s = s2[l : r]

            if sorted(sub_s) == s1:
                return True

        return False
        



        
        