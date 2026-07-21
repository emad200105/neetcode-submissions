class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ps="+DC"
        st=[]

        for op in operations:
            if op not in ps:
                st.append(int(op))
            else:
                if op=="+":
                    st.append(st[-1]+st[-2])
                elif op=="D":
                    st.append(st[-1]*2)
                else:
                    st.pop()
        sum=0

        while st:
            sum+=st.pop()
        
        return sum