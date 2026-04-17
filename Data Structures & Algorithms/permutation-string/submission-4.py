class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_ord = [0] * 26
        for char in s1:
            index = ord(char) - ord('a')
            s1_ord[index] += 1

        equal_count = 0
        i = 0
        j = len(s1) - 1
        while j < len(s2):
            print(s2[i:j+1])
            substring_ord = [0] * 26
            for char in s2[i:j+1]:
                index = ord(char) - ord('a')
                substring_ord[index] += 1
            
            for k in range(len(s1_ord)):
                if substring_ord[k] == s1_ord[k]:
                    equal_count += 1
            print(equal_count)
            if len(s1_ord) == equal_count:
                return True
            else:
                equal_count = 0
                i += 1
                j += 1
        
        return False
                    