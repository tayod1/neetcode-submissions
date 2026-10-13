class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        arr = []
        for n in freq:
            arr.append((freq[n], n))
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res


        

        
        