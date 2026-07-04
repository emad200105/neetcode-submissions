class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        visited=set()
        isIsland=0
        rows=len(grid)
        cols=len(grid[0])


        def bfs(r,c):
            que=collections.deque()
            visited.add((r,c))
            que.append((r,c))

            while que:
                row,col=que.popleft()

                for dr,dc in directions:
                    newr=row+dr
                    newc=col+dc
                    if newr in range(rows) and newc in range(cols) and grid[newr][newc]=="1" and (newr,newc) not in visited:
                        visited.add((newr,newc))
                        que.append((newr,newc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    isIsland+=1
        
        return isIsland