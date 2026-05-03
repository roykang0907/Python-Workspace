t = int(input())

for _ in range(t):
    n = int(input())
    arr = []

    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))

    arr.sort()

    chosen = 1000000007
    ans = 0

    for a, b in arr:
        if b < chosen:
            chosen = b
            ans += 1

    print(ans)
