class Solution:

    def encode(self, strs: List[str]) -> str:
        return_str = ""
        for s in strs:
            return_str += f"{len(s)}#{s}"

        return return_str

    def decode(self, s: str) -> List[str]:
        res_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            i = j + 1
            j = i + length

            chars = s[i:j]
            res_list.append(chars)

            i = j

        return res_list

