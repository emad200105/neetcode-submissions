class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=set()
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        maxi=0
        rows=len(grid)
        cols=len(grid[0])

        def bfs(r,c):
            que=collections.deque()
            que.append((r,c))
            cnt=1
            visited.add((r,c))

            while que:
                row,col=que.popleft()

                for dr,dc in directions:
                    newr=dr+row
                    newc=dc+col

                    if newr in range(rows) and newc in range(cols) and grid[newr][newc]==1 and (newr,newc) not in visited:
                        cnt+=1
                        visited.add((newr,newc))
                        que.append((newr,newc))
            
            return cnt

        for r in range(rows):
            for c in range(cols): 
                if grid[r][c]==1 and (r,c) not in visited:
                    maxi=max(maxi,bfs(r,c))
        

        return maxi