class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        maxi=0
        visited=set()
        cnt=0

        def dfs(r,c):
            nonlocal cnt
            cnt+=1
            visited.add((r,c))

            directions=[[0,1],[1,0],[0,-1],[-1,0]]
            for dr,dc in directions:
                newr=r+dr
                newc=c+dc
                if newr in range(rows) and newc in range(cols) and grid[newr][newc]==1 and (newr,newc) not in visited:
                    dfs(newr,newc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c)not in visited:
                    cnt=0
                    dfs(r,c)
                    maxi=max(maxi,cnt)
        

        
        return maxi