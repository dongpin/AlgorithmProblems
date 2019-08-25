namespace Leetcode
{
    public partial class Algorithm
    {
        private static int[][] directions = new int[][]
            {
                new int[] {1, 0},
                new int[] {0, 1},
                new int[] {-1, 0},
                new int[] {0, -1}
            };
        public static int CountNumOfIslands(char[][] grid)
        {
            var result = 0;
            for (var i = 0; i < grid.Length; i++)
            {
                for (var j = 0; j < grid[0].Length; j++)
                {
                    if (grid[i][j] == '1')
                    {
                        CountNumOfIslands_Dfs(grid, i, j);
                        result += 1;
                    }
                }
            }

            return result;
        }

        private static void CountNumOfIslands_Dfs(char[][] grid, int row, int col)
        {
            grid[row][col] = '0';

            for (var i = 0; i < 4; i++)
            {
                var newRow = row + directions[i][0];
                var newCol = col + directions[i][1];
                if (newRow >= 0 && newRow < grid.Length
                    && newCol >= 0 && newCol < grid[0].Length
                    && grid[newRow][newCol] == '1')
                {
                    CountNumOfIslands_Dfs(grid, newRow, newCol);
                }
            }
        }
    }
}