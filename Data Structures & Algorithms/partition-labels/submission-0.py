class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_map = {}; res = []
        for (i, letter) in enumerate(s):
            last_map[letter] = i
        
        i = 0; a,b = 0,0;
        for i, c in enumerate(s):
            a += 1
            b = max(b, last_map[c])

            if i == b:
                res.append(a)
                a = 0
        
        return res