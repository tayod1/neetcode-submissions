class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # use hashmap to count frequency of each element
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        arr = []

        # use a list to append tuples of (freq, n)
        for n in freq:
            arr.append((freq[n], n))

        # sort list so most frequent values at end
        arr.sort()

        res = []
        while len(res) < k:
            # dynamically update res with values
            # starting from end of arr
            res.append(arr.pop()[1])

        return res


        

        
        