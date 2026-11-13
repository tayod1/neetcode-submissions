class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        store = defaultdict(list)

        def _getCount(s):
            count_s = {}
            for c in s:
                count_s[c] = count_s.get(c, 0) + 1
            return count_s

        for s in strs:
            counter = _getCount(s)
            key = tuple(sorted(counter.items()))
            store[key].append(s)

        return list(store.values())