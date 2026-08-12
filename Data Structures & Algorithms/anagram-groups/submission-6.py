from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            ord_arr = [0] * 26
            for letter in s:
                ind = ord(letter.lower()) - ord('a')
                ord_arr[ind] += 1
            ord_arr = tuple(ord_arr)
            m[ord_arr].append(s)

        res = [m[a] for a in m]
        return res