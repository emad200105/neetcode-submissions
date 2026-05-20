class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        valid="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        while(l<=r):
            if s[l] not in valid:
                l+=1
                continue
            elif s[r] not in valid:
                r-=1
                continue
            if s[l].lower()!=s[r].lower():
                return False
            
            l+=1
            r-=1
        return True