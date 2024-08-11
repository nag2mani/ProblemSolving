def regionsBySlashes(grid):
    n = len(grid)
    # We scale up the grid by a factor of 3x to easily manage regions
    scaled_grid = [[0] * (n * 3) for _ in range(n * 3)]
    
    # Mark the scaled grid based on '/' and '\\'
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '/':
                scaled_grid[i * 3][j * 3 + 2] = 1
                scaled_grid[i * 3 + 1][j * 3 + 1] = 1
                scaled_grid[i * 3 + 2][j * 3] = 1
            elif grid[i][j] == '\\':
                scaled_grid[i * 3][j * 3] = 1
                scaled_grid[i * 3 + 1][j * 3 + 1] = 1
                scaled_grid[i * 3 + 2][j * 3 + 2] = 1

    # Function to perform DFS on the scaled grid
    def dfs(x, y):
        if x < 0 or x >= n * 3 or y < 0 or y >= n * 3 or scaled_grid[x][y] != 0:
            return
        scaled_grid[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
    
    # Counting the number of regions using DFS
    regions = 0
    for i in range(n * 3):
        for j in range(n * 3):
            if scaled_grid[i][j] == 0:
                dfs(i, j)
                regions += 1
    
    return regions

grid2 = [" /","/ "]
grid3 = [" /\\"," \\/","\\  "]
grid4 = ["/\\/\\", "\\/\\/", "/\\/\\", "\\/\\\\"]

print(regionsBySlashes(grid2))
print(regionsBySlashes(grid3))
print(regionsBySlashes(grid4))
