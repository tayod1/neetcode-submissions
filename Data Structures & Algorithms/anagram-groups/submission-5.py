class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sorted_key = "".join(sorted(s))
            res[sorted_key].append(s)

        return list(res.values())

        """
        Time Complexity -> O(m * n)
            m = number of strings
            n = average length of each string (since counting chars)
        """

            

