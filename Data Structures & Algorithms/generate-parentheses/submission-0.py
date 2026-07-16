class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res=[]

        def sol(opeN,Close,st):
            if opeN==n and Close==n:
                res.append("".join(st.copy()))
                return

            if opeN<n:
                st.append("(")
                sol(opeN+1,Close,st)
                st.pop()

            if Close<opeN:
                st.append(")")
                sol(opeN,Close+1,st)
                st.pop()
            
        sol(0,0,[])
        return res