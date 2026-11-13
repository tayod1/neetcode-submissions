class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ord() gives you a number for a character

        store = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            store[tuple(count)].append(s)

        return list(store.values())

        # Time complexity: O(n * m)
            # n is the number of words and m is the maximum word length

        # Space complexity: O(m)
            # m is the number of words, there can m groups in store
            


