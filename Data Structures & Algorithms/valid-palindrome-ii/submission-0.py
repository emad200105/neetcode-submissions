class Solution:
    def validPalindrome(self, s: str) -> bool:
        

        def checher(n):
            i,j=0,len(s)-1

            while i<j:
                if i==n:
                    i+=1
                    continue
                elif j==n:
                    j-=1
                    continue
                
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        
        res=checher(-1)
        if res: return res

        for i in range(len(s)):
            if checher(i):
                return True
        return False