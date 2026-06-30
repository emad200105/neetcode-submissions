class Solution:
    def isValid(self, s: str) -> bool:
        dt={
            ")":"(",
            "}":"{",
            "]":"["
        }

        st=[]

        for ch in s:
            if ch == "(" or ch=="{" or ch=="[":
                st.append(ch)
            elif not st  or st[-1]!=dt[ch]:
                return False
            else:
                st.pop()
        return len(st)==0