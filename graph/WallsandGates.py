from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        inBound = lambda r,c: 0<=r<len(rooms) and 0<=c<len(rooms[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        emptySpace = 2147483647
        gate = 0
        queue = deque()
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == gate:
                    queue.append((r,c))
        
        while queue:
    
            row, col = queue.popleft()
            for r,c in directions:
                nr = r + row
                nc = c + col
                if not(inBound(nr,nc)) or rooms[nr][nc] != emptySpace:
                    continue
                        
                rooms[nr][nc] = rooms[row][col] + 1
                queue.append((nr,nc))
