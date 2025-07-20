import heapq
from constants import *

def dijkstra(grid, start, end, draw_callback):
    heap = [(0, start)]
    visited = set()
    parent = {}

    while heap:
        cost, (row, col) = heapq.heappop(heap)
        if (row, col) == end:
            break
        if (row, col) in visited:
            continue
        visited.add((row, col))
        grid.grid[row][col] = "VISITED"
        draw_callback()

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            r, c = row + dr, col + dc
            if 0 <= r < ROWS and 0 <= c < COLS and grid.grid[r][c] != "WALL":
                heapq.heappush(heap, (cost + 1, (r, c)))
                parent[(r, c)] = (row, col)

    return reconstruct_path(parent, end, grid, draw_callback)

def reconstruct_path(parent, end, grid, draw_callback):
    path = []
    node = end
    while node in parent:
        path.append(node)
        node = parent[node]
    for node in path:
        grid.grid[node[0]][node[1]] = "PATH"
        draw_callback()
    return path