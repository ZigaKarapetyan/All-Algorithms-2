def is_valid(r, c, R, C):
    return 0 <= r < R and 0 <= c < C

def bfs_grid(grid, start_row, start_col):
    R=len(grid)
    C=len(grid[0])

    
    queue = [(start_row, start_col)]

    
    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[start_row][start_col] = True

   
    dR = [-1, 0, 1, 0]
    dC = [0, 1, 0, -1]

    while queue:
        r, c = queue.pop(0)
        print("Visiting:", r, c)

        
        for i in range(4):
            nr =r +dR[i]
            nc = c + dC[i]

            if is_valid(nr, nc, R, C) and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc))



grid =[
    [1,1,1],
    [1,1,1],
    [1,1,1]
]
bfs_grid(grid, 0, 0)
