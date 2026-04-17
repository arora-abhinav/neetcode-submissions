class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0
        end = len(s1) - 1
        hash_map = {}
        s1_arr = [0] * 26
        s2_arr = [0] * 26
        if len(s2) >= len(s1):
            for i in s1:
                s1_arr[ord(i) - ord('a')] += 1
            for j in range(end + 1):
                s2_arr[ord(s2[j]) - ord('a')] += 1

            while end < len(s2):
                if s1_arr != s2_arr:
                    s2_arr[ord(s2[start]) - ord('a')] -= 1
                    start += 1
                    end += 1
                    if end >= len(s2):
                        return False
                    s2_arr[ord(s2[end]) - ord('a')] += 1

                else:
                    return True
            
            return False
        return False