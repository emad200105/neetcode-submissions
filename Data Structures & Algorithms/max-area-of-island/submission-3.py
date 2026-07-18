class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        maxi=0

        def dfs(r,c):
            visited.add((r,c))
            res=1
            for dr,dc in directions:
                newr=dr+r
                newc=dc+c

                if newr in range(rows) and newc in range(cols) and grid[newr][newc]==1 and (newr,newc) not in visited:
                    res+=dfs(newr,newc)
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    res=dfs(r,c)
                    maxi=max(maxi,res)
        return maxi