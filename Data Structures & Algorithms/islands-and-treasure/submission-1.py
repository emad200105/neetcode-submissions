class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        visited=set()

        def bfs(r,c):
            que=collections.deque()

            visited.add((r,c))
            que.append((r,c))

            dis=1

            while que:
                qlen=len(que)
                for i in range(qlen):
                    row,col=que.popleft()
                    for dr,dc in directions:
                        newr=row+dr
                        newc=col+dc

                        if newr in range(rows) and newc in range(cols) and grid[newr][newc]!=-1 and grid[newr][newc]!=0 and dis<grid[newr][newc]:
                            grid[newr][newc]=dis
                            que.append((newr,newc))
                dis+=1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0 and (r,c) not in visited:
                    bfs(r,c)