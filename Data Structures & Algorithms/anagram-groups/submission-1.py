class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        res = []     

        for i, v in enumerate(strs):
            to_add = [x for x in strs if Counter(v) == Counter(x)]
            if to_add not in res:
                res.append(to_add)

        return res


        