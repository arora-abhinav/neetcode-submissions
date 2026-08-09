class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        if len(strs) == 0:
            return "None"

        for s in strs:
            string += s + "<->"
        string = string[:len(string)-3]
        string += "*"

        return string
    def decode(self, s: str) -> List[str]:
        if s is "None":
            return []
        res = s.split("<->")
        res[-1] = res[-1][:len(res[-1]) - 1]
        return res