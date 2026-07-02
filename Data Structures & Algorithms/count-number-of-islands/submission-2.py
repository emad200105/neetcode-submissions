class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows,cols=len(grid),len(grid[0])
        visited=set()
        isIslands=0

        def dfs(r,c):
            visited.add((r,c))
            directions=[[0,1],[0,-1],[1,0],[-1,0]]
                
            for dr,dc in directions:
                newr=r+dr
                newc=c+dc
                if newr in range(rows) and newc in range(cols) and grid[newr][newc]=="1" and (newr,newc) not in visited:
                    dfs(newr,newc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    dfs(r,c)
                    isIslands+=1
        
        
        return isIslands
