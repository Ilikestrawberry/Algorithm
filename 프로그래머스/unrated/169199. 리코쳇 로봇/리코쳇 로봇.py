from collections import deque

def solution(board):
    answer = 0
    rows = len(board)
    cols = len(board[0])
    rx, ry = 0, 0
    for i in range(rows):
        for j in range(cols):
            if board[i][j]=='R':
                rx, ry = i, j
                break
    
    def bfs():
        q = deque()
        q.append((rx, ry))
        visited = [[0] * cols for _ in range(rows)]
        visited[rx][ry] = 1
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        while q:
            px, py = q.popleft()
            if board[px][py] == 'G':
                # print(visited)
                return visited[px][py]
            for i in range(4):
                nx, ny = px, py
                while True:
                    nx += dx[i]
                    ny += dy[i]
                    if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 'D':
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[px][py] + 1
                    q.append((nx, ny))
        return -1
                    
    answer = bfs()
    if answer > 0:
        answer -= 1
    return answer