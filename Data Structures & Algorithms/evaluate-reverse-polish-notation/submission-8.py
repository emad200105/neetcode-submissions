class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops="+-/*"
        st=[]

        for token in tokens:
            if token not in ops:
                st.append(int(token))
            else:
                num2=st.pop()
                num1=st.pop()

                if token=="/":
                    st.append(int(num1/num2))
                elif token=="+":
                    st.append(num1+num2)
                elif token=="-":
                    st.append(num1-num2)
                else:
                    st.append(num1*num2)
        return st.pop()