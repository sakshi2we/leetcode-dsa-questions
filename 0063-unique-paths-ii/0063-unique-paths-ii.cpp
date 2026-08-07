class Solution {
public:

    int solve(int i, int j, vector<vector<int>>& grid,
              vector<vector<int>>& dp) {

        int m = grid.size();
        int n = grid[0].size();

        // Out of bounds
        if (i >= m || j >= n)
            return 0;

        // Obstacle
        if (grid[i][j] == 1)
            return 0;

        // Destination reached
        if (i == m - 1 && j == n - 1)
            return 1;

        // Already computed
        if (dp[i][j] != -1)
            return dp[i][j];

        int down = solve(i + 1, j, grid, dp);
        int right = solve(i, j + 1, grid, dp);

        return dp[i][j] = down + right;
    }

    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {

        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();

        // If starting cell is blocked
        if (obstacleGrid[0][0] == 1)
            return 0;

        vector<vector<int>> dp(m, vector<int>(n, -1));

        return solve(0, 0, obstacleGrid, dp);
    }
};