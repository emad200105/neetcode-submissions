class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited=set()
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        rows=len(grid)
        cols=len(grid[0])


        que=collections.deque()

        def bfs():
            minutes=0
            while que:
                qlen=len(que)
                for i in range(qlen):
                    dr,dc=que.popleft()
                    for direction in directions:
                        r=dr+direction[0]
                        c=dc+direction[1]
                        if r in range(rows) and c in range(cols) and grid[r][c]==1 and (r,c) not in visited:
                            grid[r][c]=2
                            visited.add((r,c))
                            que.append((r,c))
                if que:
                    minutes+=1
            return minutes

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2 and (r,c) not in visited:
                    que.append((r,c))
                    visited.add((r,c))
        
        minutes=bfs()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    return -1

        return minutes