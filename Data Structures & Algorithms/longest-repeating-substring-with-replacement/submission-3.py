class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0
        res = 0
        frequency_map = defaultdict(int)
        while end < len(s):
            frequency_map[s[end]] += 1


            while end - start + 1 - max(frequency_map.values()) > k:
                frequency_map[s[start]] -= 1
                start += 1
            
            res = max(res, end - start + 1)
            end += 1
        
        return res
        