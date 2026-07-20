class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = min(len(word1), len(word2))
        
        ans = ""
        for i in range(m):
            a = word1[i]
            b = word2[i]

            ans += a+b
        
        if len(word1) > m:
            ans += word1[m:]
        else:
            ans += word2[m:]

        return ans

        