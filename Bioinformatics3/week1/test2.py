coins = [1, 4, 5]

dp = [999] * 24
dp[0] = 0

for i in range(1, 24):
    for s in coins:
        if i >= s:
            dp[i] = min(dp[i], dp[i - s] + 1)

for i in range(13, 24):
    print(dp[i], end = ' ')
