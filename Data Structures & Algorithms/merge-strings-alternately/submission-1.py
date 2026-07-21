class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""

        l,r=0,0

        while l<len(word1) or r<len(word2):
            w1=word1[l] if l<len(word1) else ""
            w2=word2[r] if r<len(word2) else ""

            res+=w1+w2
            l+=1
            r+=1
        return res