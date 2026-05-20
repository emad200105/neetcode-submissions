class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set()
        for num in nums:
            if num not in st:
                st.add(num)
        maxi=0
        for num in st:
            curr=1
            looking=num+1
            while looking in st:
                curr+=1
                looking+=1
            maxi=max(curr,maxi)
        return maxi