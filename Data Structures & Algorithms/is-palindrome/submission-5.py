class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1

        valid="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

        while i<j:
            if s[i] not in valid:
                i+=1
                continue
            elif s[j] not in valid:
                j-=1
                continue
            
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1

        return True