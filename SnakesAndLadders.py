class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board) - 1
        queue = deque([(n, 0, 1, 0)])
        visited = {1 : 0}
        isNotGoingNormally = {n: False}
        for i in range(n - 1, -1, -1):
            isNotGoingNormally[i] = not isNotGoingNormally[i + 1]
   
        def returnFixedPosition(num):
            row = (num - 1) // (n + 1)
            row = n - row
            col = (num - 1) % (n + 1)
            if isNotGoingNormally[row]:
                col = n - col


            return (row, col)

        while queue:
            row, col, num, level = queue.popleft()
            if num == (n + 1) ** 2:
                return level
            
            for next_num in range(num + 1, min(num + 7,((n + 1) ** 2) + 1)):
                nr, nc = returnFixedPosition(next_num)
                lowercost = next_num not in visited or level+1 < visited[next_num]

                if board[nr][nc] != -1:
                    fixed_row, fixed_col = returnFixedPosition(board[nr][nc])
                    if board[nr][nc] not in visited or level + 1 < visited[board[nr][nc]]:
                        queue.append((fixed_row, fixed_col, board[nr][nc], level + 1))
                        visited[board[nr][nc]] = level + 1
                        visited[next_num] = level + 1 

                elif board[nr][nc] == -1 and lowercost:
                    visited[next_num] = level + 1
                    queue.append((nr, nc, next_num, level + 1))



        return -1 
