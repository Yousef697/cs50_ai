from queue import PriorityQueue

def a_star(g):
    n, m = len(g), len(g[0])

    start_x, start_y = -1, -1
    end_x, end_y = -1, -1

    for i in range(n):
        for j in range(m):
            if g[i][j] == 'A':
                start_x, start_y = i, j
            if g[i][j] == 'B':
                end_x, end_y = i, j

    def valid(x, y):
        return 0 <= x and x < n and 0 <= y and y < m and g[x][y] != '#' and not visited[x][y]
    
    def h(x, y):
        return abs(x - end_x) + abs(y - end_y)
    def k(cells):
        return cells + 1
    
    pq = PriorityQueue()
    visited = [[False] * m for i in range(n)]
    parent = [[(-1, -1) for j in range(m)] for i in range(n)]
    pq.put((0, 0, start_x, start_y, start_x, start_y))

    while not pq.empty():
        cost, cells, cur_x, cur_y, parent_x, parent_y = pq.get()

        if visited[cur_x][cur_y]:
            continue

        # print(cur_x, cur_y)
        visited[cur_x][cur_y] = True
        parent[cur_x][cur_y] = (parent_x, parent_y)
        if cur_x == end_x and cur_y == end_y:
            break

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = cur_x + dx, cur_y + dy
            if valid(nx, ny):
                pq.put((h(nx, ny) + k(cells), k(cells), nx, ny, cur_x, cur_y))

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
path = a_star(grid)
print(len(path))
print(path)
