class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])

        visited=set()

        directions=[[0,1],[1,0],[0,-1],[-1,0]]

        def bfs(r,c):
            que=collections.deque()
            visited.add((r,c))
            que.append((r,c))
            distance=0
            while que:
                distance+=1
                qlen=len(que)
                for i in range(qlen):
                    r,c=que.popleft()
                    for dr,dc in directions:
                        newr=dr+r
                        newc=dc+c

                        if newr in range(rows) and newc in range(cols) and grid[newr][newc]!=-1 and grid[newr][newc]!=0 and distance<grid[newr][newc]:
                            grid[newr][newc]=distance
                            que.append((newr,newc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0 and (r,c) not in visited:
                    bfs(r,c)

        