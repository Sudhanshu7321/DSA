MOD = 10**9 + 7

def max_path_sum(n, grid):
    if n == 0:
        return 0
    
    # Initialize the dp table with zeros
    dp = [[0] * 2 for _ in range(n)]
    
    # Initialize the first row of dp table
    dp[0][0] = grid[0][0]
    dp[0][1] = grid[0][1]
    
    # Fill the dp table
    for i in range(1, n):
        for j in range(2):
            max_sum = 0
            for k in range(2):
                if grid[i][j] > grid[i-1][k]:
                    max_sum = max(max_sum, dp[i-1][k] + grid[i][j])
            dp[i][j] = max_sum % MOD
    
    # Find the maximum value in the last row of dp table
    result = max(dp[n-1][0], dp[n-1][1])
    
    return result

# Reading input
n = int(input().strip())
grid = []

for _ in range(n):
    grid.append(list(map(int, input().strip().split())))

# Calculate and print the maximum path sum
print(max_path_sum(n, grid))
