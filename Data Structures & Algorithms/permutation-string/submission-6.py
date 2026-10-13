class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False

        # use Counter to track num of characters
        s1_counts = Counter(s1)
        window_counts = Counter(s2[:n1])

        # Check the very first window
        if s1_counts == window_counts:
            return True

        # slide the window across s2
        for i in range(n1, n2):
            char_in = s2[i] # character entering the window
            char_out = s2[i - n1] # character leaving the window

            window_counts[char_in] += 1
            
            # decrease count of the char leaving
            window_counts[char_out] -= 1

            # remove char if it hits 0
            if window_counts[char_out] == 0:
                del window_counts[char_out]

            if s1_counts == window_counts:
                return True

        return False
        



        
        