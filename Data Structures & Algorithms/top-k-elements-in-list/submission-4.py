class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            store[n] = store.get(n, 0) + 1
        
        for n, cnt in store.items():
            freq[cnt].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        