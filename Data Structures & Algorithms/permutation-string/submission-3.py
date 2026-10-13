class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)

        for l in range(len(s2)):
            r = l + window_size
            sub_s = s2[l : r]
            print(sub_s)
            if sorted(sub_s) == sorted(s1):
                return True

        return False
        



        
        