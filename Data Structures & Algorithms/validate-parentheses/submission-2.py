class Solution:
    def isValid(self, s: str) -> bool:
        dt={
            ")":"(",
            "]":"[",
            "}":"{"
        }

        st=[]

        for c in s:
            if c in "({[":
                st.append(c)
            else:
                if not st or st[-1]!=dt[c]:
                    return False
                else:
                    st.pop()
        return not st