class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res+=i
        arr = []

        for j in strs:
            arr.append(len(j))
        
        res += " "
        for k in arr:
            res += "*"+str(k)
        
        print (res)
        return res

    def decode(self, s: str) -> List[str]:
        ind = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                ind = i
                break
        arr = []
        # lengths = s[i:]
        # lengths.strip(): Removes spaces (for safety)
        # parts = lengths.split(): returns ["1, 23]
        
        for j in range(ind + 1, len(s)):
            if s[j] == '*':
                k = j + 1
                res = ""
                while k <= len(s) - 1 and s[k] != '*':
                    res += s[k]
                    k += 1
                arr.append(int(res))
        
        print(arr)

        for i in range(0, len(arr)):
            if i != 0:
                arr[i] += arr[i-1]

        ind = 0
        str_arr = []
        for num in arr:
            k = s[ind:num]
            ind = num
            str_arr.append(k)
        
        return str_arr
        # lengths = 
