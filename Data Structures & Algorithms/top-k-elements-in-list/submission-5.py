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
        

        # Time Complexity: O(n)
            # the buckets share at most n values total

        # Space Complexity: O(n)
            # freq allocates n + 1 buckets, store holds at most n entries

