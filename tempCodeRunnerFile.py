input = sys.stdin.readline

n = int(input().rstrip())
arr = [0]+[int(input().rstrip()) for _ in range(n)]

dp = [[arr[i], arr[i]] for i in range(n+1)]

for i in range(2, n+1):
    dp[i][0] += dp[i-1][1]
    dp[i][1] += max(dp[i-2])

print(max(dp[-1]))