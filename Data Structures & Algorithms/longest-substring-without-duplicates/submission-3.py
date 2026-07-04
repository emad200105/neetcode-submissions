class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi=0
        l,r=0,0
        st=set()

        while r<len(s):
            while s[r] in st:
                st.remove(s[l])
                l+=1
            st.add(s[r])
            maxi=max(maxi,len(st))
            r+=1
        return maxi