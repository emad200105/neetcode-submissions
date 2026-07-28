class Solution:
    def isValid(self, strs: str) -> bool:
        dt={
            ")":"(",
            "}":"{",
            "]":"["
        }
        st=[]

        for s in strs:
            if s in "({[":
                st.append(s)
            else:
                if not st or st[-1]!=dt[s]:
                    return False
                else:
                    st.pop()
        return len(st)==0