from collections import deque
import copy

def bfs(x, y, target, maps, graph):
    n_rows = len(maps)
    n_cols = len(maps[0])
    # graph 객체 내부값 바뀌지 않도록
    graph = copy.deepcopy(graph)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 방문 기록
    visited = [[0 for _ in m] for m in maps]
    visited[x][y] = 1
    queue = deque()
    queue.append((x, y))
    # 경우에 따라 사용 가능한 위치 저장
    if target == 'L':
        avaliable = 'E'
    elif target == 'E':
        avaliable = 'S'
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n_rows - 1 or ny < 0 or ny > n_cols - 1:
                continue
            if visited[nx][ny] == 1 or maps[nx][ny] == 'X':
                continue
            if maps[nx][ny] == 'O' or maps[nx][ny] == avaliable:
                visited[nx][ny] = 1
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
            if maps[nx][ny] == target:
                return graph[x][y]
    return -1

def solution(maps):
    graph = []
    for idx, r in enumerate(maps):
        if 'S' in r:
            x = idx
            y = r.index('S')
        if 'L' in r:
            lx = idx
            ly = r.index('L')

        r = r.replace('S', '1')
        r = r.replace('O', '1')
        r = r.replace('L', '1')
        r = r.replace('E', '1')
        r = r.replace('X', '0')
        graph.append(list(map(int, r)))

    s_to_l = bfs(x, y, 'L', maps, graph)
    l_to_e = bfs(lx, ly, 'E', maps, graph)
    
    if s_to_l == -1 or l_to_e == -1:
        return -1
    else:
        return s_to_l + l_to_e