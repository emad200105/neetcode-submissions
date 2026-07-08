class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        visited=set()

        rows=len(grid)
        cols=len(grid[0])

        total=0

        def dfs(r,c):
            visited.add((r,c))
            res=0

            for direction in directions:
                dr=r+direction[0]
                dc=c+direction[1]

                if dr in range(rows) and dc in range(cols) and grid[dr][dc]==1 and (dr,dc) not in visited:
                    res+=dfs(dr,dc)
                elif dr not in range(rows) or dc not in range(cols) or grid[dr][dc]==0 or (dr,dc) not in visited:
                    res+=1
            return res
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    total=dfs(r,c)
                    

        return total