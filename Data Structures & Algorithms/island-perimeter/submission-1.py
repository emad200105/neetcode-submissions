class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        visited=set()
        res=0


        def dfs(r,c):
            nonlocal res
            visited.add((r,c))
            for dr,dc in directions:
                newr=dr+r
                newc=dc+c

                if newr not in range(rows) or newc not in range(cols) or grid[newr][newc]==0:
                    res+=1
                if newr in range(rows) and newc in range(cols) and grid[newr][newc]==1 and (newr,newc) not in visited:
                    dfs(newr,newc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    dfs(r,c)
        return res