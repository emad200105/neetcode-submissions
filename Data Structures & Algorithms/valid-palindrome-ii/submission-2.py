class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1

        while i<j:
            if s[i]!=s[j]:
                left=s[:i]+s[i+1:]
                right=s[:j]+s[j+1:]

                if left==left[::-1] or right ==right[::-1]:
                    return True
                else:
                    return False
            i+=1
            j-=1


        return True