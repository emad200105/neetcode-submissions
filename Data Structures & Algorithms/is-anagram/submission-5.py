class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chk=[0]*26
        if len(s)!=len(t):
            return False
        
        for i in range(len(s)):
            chk[ ord(s[i]) - ord('a') ]+=1
            chk[ ord(t[i]) - ord('a') ]-=1

        return [0]*26 == chk