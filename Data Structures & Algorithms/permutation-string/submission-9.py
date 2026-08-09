class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def obtain_arr(string):
            str_arr = [0] * 26
            for s in string:
                str_arr[ord(s.upper()) - ord('A')] += 1
            return str_arr
        
        s1_arr = obtain_arr(s1)
        i, j = 0, len(s1) - 1
        s2_arr = obtain_arr(s2[i: j+1])
        counts = 0
        while s1_arr != s2_arr and j < len(s2) - 1:
            s2_arr[ord(s2[i].upper()) - ord('A')] -= 1
            i,j = i + 1, j + 1
            s2_arr[ord(s2[j].upper()) - ord('A')] += 1
            print(s2_arr)
            counts += 1

        return s1_arr == s2_arr