class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        visited=set()
        isIsland=0
        rows=len(grid)
        cols=len(grid[0])


        def dfs(r,c):
            visited.add((r,c))


            for dr,dc in directions:
                newr=r+dr
                newc=c+dc
                if newr in range(rows) and newc in range(cols) and grid[newr][newc]=="1" and (newr,newc) not in visited:
                    dfs(newr,newc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    dfs(r,c)
                    isIsland+=1
        
        return isIsland