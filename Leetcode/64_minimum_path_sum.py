class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        经典动态规划问题

        '''
        if not grid or len(grid) == 0:
            return 0

        row = len(grid)
        col = len(grid[0]) if row else 0

        for i in range(1, col):
            grid[0][i] += grid[0][i - 1]

        for i in range(1, row):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]