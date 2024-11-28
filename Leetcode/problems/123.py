def maxProfit(prices, k=2):
    n = len(prices)
    if (n) <= 1:
        return 0
    if k > n//2:
        max_profit = 0
        for i in range(1, n):
            if prices[i] - prices[i-1] > 0:
                max_profit += prices[i] - prices[i-1]
        return max_profit

    dp = [[0]* n for _ in range(k+1)]

    for i in range(1, k+1):
        maxDiff = - prices[0]
        for j in range(1, n):
            dp[i][j] = max(dp[i][j-1], prices[j] + maxDiff)
            maxDiff = max(maxDiff, dp[i-1][j]- prices[j])
    return dp[k][n-1]