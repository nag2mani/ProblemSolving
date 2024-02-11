class Solution:
    def cherryPickup(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])

        # @lru_cache(None)
        #why after adding above line take less time than not adding
        
        def dp(row, col1, col2):
            if row == rows:
                return 0
            cherries = grid[row][col1] + (grid[row][col2] if col1 != col2 else 0)
            max_cherries = 0
            for d1 in [-1, 0, 1]:
                for d2 in [-1, 0, 1]:
                    new_col1, new_col2 = col1 + d1, col2 + d2
                    if 0 <= new_col1 < cols and 0 <= new_col2 < cols:
                        max_cherries = max(max_cherries, dp(row + 1, new_col1, new_col2))
            return cherries + max_cherries
        
        return dp(0, 0, cols - 1)