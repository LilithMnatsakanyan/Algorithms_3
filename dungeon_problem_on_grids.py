dungeon = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '.', '.', '.'],
    ['#', '.', '#', 'E', '.', '#', '.']
]
from collections import deque
R = len(dungeon)
C = len(dungeon[0])

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * C for _ in range(R)]
prev = [[None] * C for _ in range(R)]

start = None
end = None
for r in range(R):
    for c in range(C):
        if dungeon[r][c] == 'S':
            start = (r, c)
        if dungeon[r][c] == 'E':
            end = (r, c)

# BFS
def bfs():
    rq = deque([start])
    visited[start[0]][start[1]] = True
    steps = 0
    found = False

    #  BFS
    while rq and not found:
        size = len(rq)
        for _ in range(size):
            r, c = rq.popleft()

            if (r, c) == end:
                found = True
                break

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and dungeon[nr][nc] != '#':
                    visited[nr][nc] = True
                    prev[nr][nc] = (r, c)
                    rq.append((nr, nc))

        steps += 1

    if found:
        return steps
    else:
        return -1

def reconstruct_path():
    path = []
    r, c = end
    while (r, c) != start:
        path.append((r, c))
        r, c = prev[r][c]
    path.append(start)
    return path[::-1]

steps = bfs()
if steps == -1:
    print("Escape is not possible!")
else:
    print(f"Escape is possible! It will take {steps} steps.")
    path = reconstruct_path()
    print("Shortest path to escape:", path)
