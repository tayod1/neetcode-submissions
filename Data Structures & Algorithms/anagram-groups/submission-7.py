class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            # sort the string
            sorted_key = "".join(sorted(s))

            # use the sorted string as a key
            # append s to resolved key
            res[sorted_key].append(s)

        return list(res.values())
