class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1); dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordSet:
                if i + len(w) <= len(s):
                    if s[i: i + len(w)] == w:
                        dp[i] = dp[i + len(w)]
                
                    if dp[i] == True: 
                        break
        
        return dp[0]
