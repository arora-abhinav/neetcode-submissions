class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def obtain_arr(string):
            str_arr = [0] * 26
            for s in string:
                str_arr[ord(s.upper()) - ord('A')] += 1
            return str_arr
        
        s1_arr = obtain_arr(s1)
            
        i, j = 0, len(s1) - 1
        while j < len(s2):
            substring = s2[i: j + 1]
            substring_arr = obtain_arr(substring)
            if s1_arr == substring_arr:
                return True
            i += 1
            j += 1
        
        return False