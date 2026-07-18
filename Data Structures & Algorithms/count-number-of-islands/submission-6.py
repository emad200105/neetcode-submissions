class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        visited=set()
        que=collections.deque()
        islands=0

        def bfs(r,c):
            que.append((r,c))
            visited.add((r,c))

            while que:
                row,col=que.popleft()
                for dr,dc in directions:
                    newr=dr+row
                    newc=dc+col

                    if newr in range(rows) and newc in range(cols) and grid[newr][newc]=="1" and (newr,newc) not in visited:
                        visited.add((newr,newc))
                        que.append((newr,newc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        return islands