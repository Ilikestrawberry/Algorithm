from collections import deque

def dfs(x, y, visited, maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    cnt = int(maps[x][y])
    visited[x][y] = True
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx and nx < len(maps) and 0 <= ny and ny < len(maps[0]) and not visited[nx][ny]:
                cnt += int(maps[nx][ny])
                visited[nx][ny] = True
                queue.append((nx, ny))
    return cnt

def solution(maps):
    answer = []
    visited = [[n.isalpha() for n in r] for r in maps]
    
    for i1, r in enumerate(maps):
        for i2, c in enumerate(r):
            if c != 'X' and not visited[i1][i2]:
                answer.append(dfs(i1, i2, visited, maps))

    if not answer:
        return [-1]
    
    answer = [n for n in answer if str(n).isdigit()]
    answer = sorted(answer)

    return answer