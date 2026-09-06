class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        positions = {}
        for index, letter in enumerate(s):
            positions[letter] = index
        
        res = []; cur_max = 0
        i = 0
        for j in range(len(s)):
            cur_max = max(cur_max, positions[s[j]])
            if j == cur_max:
                res.append(j - i + 1)
                i = j + 1
        
        return res