class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

        i,j=0,len(s)-1

        while i<j:
            if s[i] not in valid:
                i+=1
                continue
            elif s[j] not in valid:
                j-=1
            elif s[i].lower()!=s[j].lower():
                return False
            else:
                i+=1
                j-=1
        return True