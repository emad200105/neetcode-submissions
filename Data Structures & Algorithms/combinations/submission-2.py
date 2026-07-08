class Solution:
    def combine(self, n: int, m: int) -> List[List[int]]:
        res=[]

        def dfs(i,arr):
            if len(arr)==m:
                res.append(arr.copy())
                return
            
            for k in range(i,n+1):
                arr.append(k)
                dfs(k+1,arr)
                arr.pop()
        dfs(1,[])
        return res