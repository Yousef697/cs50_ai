from collections import deque
    
def bfs(g):
    n, m = len(g), len(g[0])
    start_x, start_y = -1, -1
    end_x, end_y = -1, -1

    for i in range(n):
        for j in range(m):
            if g[i][j] == 'A':
                start_x, start_y = i, j
            if g[i][j] == 'B':
                end_x, end_y = i, j

    visited = [[False] * m for i in range(n)]
    parent = [[(-1, -1) for j in range(m)] for i in range(n)]

    def valid(x, y):
        return 0 <= x and x < n and 0 <= y and y < m and g[x][y] != '#' and not visited[x][y]
    
    q = deque()
    q.append((start_x, start_y))

    while len(q) != 0:
        cur_x, cur_y = q.popleft()

        if cur_x == end_x and cur_y == end_y:
            break

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = cur_x + dx, cur_y + dy
            if valid(nx, ny):
                visited[nx][ny] = True
                parent[nx][ny] = (cur_x, cur_y)
                q.append((nx, ny))

    if not visited[end_x][end_y]:
        return [(-1, -1)]
    
    path = [(end_x, end_y)]
    while (start_x, start_y) != (end_x, end_y):
        px, py = parent[end_x][end_y]
        path.append((px, py))
        end_x, end_y = px, py
    return path[::-1]

n, m = map(int, input().split())
grid = [[] for i in range(n)]
for i in range(n):
    grid[i] = input()
path = bfs(grid)
print(len(path))
print(path)
