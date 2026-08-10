from collections import defaultdict, deque
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        obtained = set()
        obtained_counter = defaultdict(int)
        best_len = float('inf')
        first, last = 0, 0
        l, r = 0, 0
        while r < len(s):
            if s[r] in t_counter:
                obtained_counter[s[r]] += 1
                if t_counter[s[r]] == obtained_counter[s[r]]:
                    obtained.add(s[r])
            
            if len(obtained) == len(t_counter):
                while l <= r and len(obtained) == len(t_counter):
                    if best_len > (r - l + 1):
                        best_len = r - l + 1
                        first = l
                        last = r
                    if s[l] in obtained_counter:
                        obtained_counter[s[l]] -= 1
                        if obtained_counter[s[l]] < t_counter[s[l]]:
                            obtained.remove(s[l])
                    l += 1
            r+= 1

        return s[first: last + 1] if best_len != float('inf') else ""