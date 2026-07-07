class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st=[]
        for op in operations:
            if op.lstrip("-").isdigit():
                st.append(int(op))
            elif op=="D":
                st.append(st[-1]*2)
            elif op=="C":
                st.pop()
            else:
                st.append((st[-1]+st[-2]))
        
        sum=0
        for num in st:
            sum+=num
        return sum