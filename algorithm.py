'''n,m = map(int,input().split())

rs=[]
chk=[False] * (n+1)

def recur(num):
    if num==m:
        print(' '.join(map(str, rs)))
    for i in range(1,n+1):
        if chk[i]==False:
            chk[i]=True
            rs.append(i)
            recur(num+1)
            chk[i]=False
            rs.pop()
recur(0)'''
'''def dfs(n,sm,cnt):
    global ans
    if n==N:
        if sm==S and cnt>0:
            ans+=1
        return
    dfs(n+1,sm+lst[n],cnt+1)
    dfs(n+1,sm,cnt)

N,S=map(int, input().split())
lst=list(map(int, input().split()))
ans=0
dfs(0,0,0)
print(ans)'''
'''n = int(input())
dp = [x for x in range (n+1)]
for i in range(1,n+1):
    for j in range(1,i):
        if j*j > i :
            break
        if dp[i] > dp[i-j*j] + 1 :
            dp[i] = dp[i-j*j] + 1
print(dp[n])'''
#2025/10/25
#Greedy Algorithm
#11399 ATM
'''n=int(input())
l=list(map(int, input().split()))
s=[]

l.sort()
a=0

for i in range(n):
    a+=l[i]
    s.append(a)
print(sum(s))'''
#2720 세탁소 사장 동혁
'''t = int(input())

for _ in range(t):
    change = int(input())
    quarters = change // 25
    change %= 25
    dimes = change // 10
    change %= 10
    nickels = change // 5
    change %= 5
    pennies = change
    print(quarters, dimes, nickels, pennies)'''
#11047 동전 0
'''n,k=map(int,input().split())
l=[]
x=0

for _ in range(n):
    a=int(input())
    l.append(a)
    
l.reverse()
for i in l:
    x+=k//i
    k%=i
print(x)'''
#1931 회의실    정
'''import sys
input=sys.stdin.readline

n=int(input())  
meetings=[]

for i in range(n):
    start, end=map(int, input().split())
    meetings.append((end, start))
    
meetings.sort()

count=0
last_end=0

for end, start in meetings:
    if start>=last_end:
        count+=1
        last_end=end

print(count)'''
#2025/10/27
#1541 잃어버린 괄호
'''s=input().split("-")

sums=[]
for p in s:
    num_sum=sum(map(int, p.split('+')))
    sums.append(num_sum)

result=sums[0]
for s in sums[1:]:
    result-=s
print(result)'''
#13305 주유소
'''n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]
cost = 0

for i in range(n-1):
    cost += min_price * dist[i]
    if price[i+1] < min_price:
        min_price = price[i+1]

print(cost)'''
#2750 수 정렬하기
'''n=int(input())
l=[]

for _ in range(n):
    i=int(input())
    l.append(i)

l.sort()

for ii in l:
    print(ii)'''
#2798번 블랙잭
'''n, m=map(int, input().split())
card=list(map(int, input().split()))

best=0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            total=card[i]+card[j]+card[k]

            if total<=m and total>best:
                best = total

print(best)'''
#2231 분해합
'''n=int(input())

result=0

for i in range(1, n + 1):
    s=i+sum(map(int, str(i)))
    if s==n:
        result=i
        break

print(result)'''
#18352 특정 거리의 도시 찾기
#bfs로 풀기

#정준의 쌤 문제 (부분 배낭 문제)
'''N, W=map(int, input().split())
l=[]
v_l=[]
a=0
f=0

for _ in range(N):
    m=list(map(int, input().split()))
    l.append(m)

for i in range(N):
    v=l[i][1]/l[i][0]
    t=(v, l[i][0])
    v_l.append(t)

v_l.sort(reverse=True)

for i in range(N):
    if a+v_l[i][1]<W:
        a+=v_l[i][1]
        f+=l[i][1]
    else:
        b=W-a
        x=v_l[i][0]*b
        f+=x

print(f)'''
#1788 피보나치 수의 확장
'''n=int(input())
mod=1000000000

if n==0:
    print(0)
    print(0)
else:
    a, b = 0, 1
    for i in range(abs(n)-1):
        a, b=b, (a+b)%mod

    f=b

    if n<0 and abs(n)%2==0:
        f=-f

    if f>0:
        print(1)
    elif f==0:
        print(0)
    else:
        print(-1)

    print(abs(f))'''
#27300X 그리디한 허브
'''N, M = map(int, input().split())

graph=[[] for _ in range(N + 1)]

for _ in range(M):
    a, b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
covered = [False] * (N + 1)
selected_hubs = []

while True:
    all_covered = True
    for i in range(1, N + 1):
        if not covered[i]:
            all_covered = False
            break
    
    if all_covered:
        break

    best_hub = 0
    max_new_cover = 0
    
    for hub in range(1, N + 1):
        new_cover_count = 0

        if not covered[hub]:
            new_cover_count += 1

        for neighbor in graph[hub]:
            if not covered[neighbor]:
                new_cover_count += 1

        if new_cover_count > max_new_cover:
            max_new_cover = new_cover_count
            best_hub = hub
        elif new_cover_count == max_new_cover and hub < best_hub:
            best_hub = hub

    selected_hubs.append(best_hub)
    
    covered[best_hub] = True
    for neighbor in graph[best_hub]:
        covered[neighbor] = True'''
#5585번 거스름돈
'''p=1000-int(input())

m=[500, 100, 50, 10, 5, 1]
r=0

for i in m:
    r+=p//i
    p%=i

print(r)'''
#1789번 수들의 합
'''n=int(input())

w=0
t=0

while t<=n:
    w+=1
    t+=w

print(w-1)'''
#17618번 신기한 수
'''import sys
input = sys.stdin.readline

N = int(input())
ans = 0

for i in range(1, N + 1):
    tmp = i
    s = 0
    while tmp:
        s += tmp % 10
        tmp //= 10
    if i % s == 0:
        ans += 1

print(ans)'''
'''n=4
goods=[[6, 30], [5, 10], [4, 40], [3, 50]]
knap=[[0 for _ in range(11)] for _ in range(n+1)]

for i in range(1, 11):
    for j in range(1, n+1):
        if goods[j][0]>i:
            knap[j][i]=knap[j][i-1]
        else:
            knap[j][i]=max(knap[j][i-goods[j][0]]+goods[j][1], knap[j][i-1])
            
print(knap[4][10])'''
#2025/12/6
#1535번 안녕
'''n=int(input())
health=list(map(int, input().split()))
joy=list(map(int, input().split()))
asdf=[0]*101

for i in range(n):
    for j in range(100, health[i], -1):
        asdf[j]=max(asdf[j], asdf[j-health[i]]+joy[i])

print(asdf[100])'''
'''import sys
sys.setrecursionlimit(10**6)

n=int(input())
edges=[]
for __ in range(n-1):
    asdf=tuple(map(int, input().split()))
    edges.append(asdf)

#인접 리스트
graph=[[] for _ in range(n+1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a) #무방향 트리

parent=[0]*(n+1)
depth=[0]*(n+1)
visited=[False]*(n+1)

def dfs(v, d):
    visited[v]=True
    depth[v]=d
    for nv in graph[v]:
        if not visited[nv]:
            parent[nv]=v
            dfs(nv, d+1)
            
def preorder_dfs(v, pre):
    visited[v]=True
    pre.append(v)
    for nv in graph[v]:
        if not visited[nv]:
            preorder_dfs(nv, pre)
            
def inorder_dfs(v,pre):
    visited[v]=True
    for nv in graph[v]:
        pre.append(nv)
        inorder_dfs(nv,pre)
        
def postorder_dfs(v,pre):
    visited[v]=True
    for nv in graph[v]:
        if not visited[nv]:
            pre.append(nv)
            postorder_dfs(nv,pre)

root=1
parent[root]=0 #루트는 부모 없음
dfs(root, 0)

for i in range(2, n+1):
    print(parent[i])'''
'''import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

# 인접 리스트
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n + 1)
depth = [0] * (n + 1)
visited = [False] * (n + 1)

def dfs(v, d):
    visited[v] = True
    depth[v] = d
    for nv in graph[v]:
        if not visited[nv]:
            parent[nv] = v
            dfs(nv, d + 1)

dfs(1, 0)

for i in range(2, n + 1):
    print(parent[i])'''
'''n=int(input())

tree={}

for _ in range(n):
    a,b,c=input().split()
    tree[a]=(b,c)

def preorder(v):
    if v=='.':
        return
    print(v,end='')
    preorder(tree[v][0])
    preorder(tree[v][1])

def inorder(v):
    if v=='.':
        return
    inorder(tree[v][0])
    print(v,end='')
    inorder(tree[v][1])

def postorder(v):
    if v=='.':
        return
    postorder(tree[v][0])
    postorder(tree[v][1])
    print(v,end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')'''

#25516번 거리가 k이하인 트리 노드에서 사과 수확하기
'''import sys
sys.setrecursionlimit(10**6)

n,k=map(int,input().split())

graph=[[] for _ in range(n)]

for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

apple=list(map(int,input().split()))
visited=[False]*n
cnt=0

def dfs(v,depth):
    global cnt
    visited[v]=True
    
    if depth<=k and apple[v]==1:
        cnt+=1
    
    for nv in graph[v]:
        if not visited[nv]:
            dfs(nv,depth+1)

dfs(0,0)
print(cnt)'''
#2941번 크로아티아 알파벳
'''s = input().strip()

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for c in croatia:
    s = s.replace(c, "*")

print(len(s))'''
#16953번 A -> B
'''a, b = map(int, input().split())

cnt = 1

while b > a:
    if b % 2 == 0:
        b //= 2
    elif b % 10 == 1:
        b //= 10
    else:
        print(-1)
        exit()
    cnt += 1

if b == a:
    print(cnt)
else:
    print(-1)'''
#DPCoinChange 예시 코드
'''from copy import deepcopy

def make_change(n, d):
    c = [999 for x in range(n+2)]
    c[0] = 0 
    p = [[] for x in range(n+2)]  # 사용된 동전 출력 위해
    for j in range(1, n+1):
        p[j] = []
        for i in range(len(d)):
            if d[i] <= j and c[j-d[i]]+1 < c[j]:
                c[j] = c[j-d[i]] + 1
                p[j] = deepcopy(p[j-d[i]])   # j원을 새 동전으로 거스르고 남은 액수에 대한 사용된 동전들
                p[j].append(d[i])     # 새 동전 추가                     
    return c, p


coins = [16, 10, 5, 1]  # 동전 세트
N = 20  # 거스름 돈
num_coins, used_coins = make_change(N, coins)
# 결과 출력
for i in range(N+1):
    print('%3d' % i, end='')
print()
for i in range(N+1):
    print('%3d' % num_coins[i], end='')

print()

print('거스름돈 %d에 대한 최소 동전 수 = %d' % (N, num_coins[N]))
print('사용된 동전:', used_coins[N])'''
#2294번 동전 2
'''def make_change(k, d):
    INF = 10**7
    c = [INF] * (k + 1)
    c[0] = 0

    for j in range(1, k + 1):
        for coin in d:
            if coin <= j:
                c[j] = min(c[j], c[j - coin] + 1)

    return c


n, k = map(int, input().split())
l = []

for _ in range(n):
    l.append(int(input()))

asdf = make_change(k, l)

print(asdf[k] if asdf[k] != 10**7 else -1)'''
#2091번 동전 문제
'''X, A, B, C, D = map(int, input().split())

best = -1
ans = (0, 0, 0, 0)

for q in range(min(D, X // 25) + 1):
    for d in range(min(C, (X - 25*q) // 10) + 1):
        rem = X - 25*q - 10*d
        if rem < 0:
            continue

        n = max(0, (rem - A + 4) // 5)

        if n > B:
            continue

        c = rem - 5*n
        if c < 0 or c > A:
            continue

        total = c + n + d + q
        if total > best:
            best = total
            ans = (c, n, d, q)

if best == -1:
    print(0, 0, 0, 0)
else:
    print(*ans)'''
#1744번 수 묶기
'''n = int(input())

pos = []
neg = []
ones = 0
zeros = 0

for _ in range(n):
    x = int(input())
    if x > 1:
        pos.append(x)
    elif x == 1:
        ones += 1
    elif x == 0:
        zeros += 1
    else:
        neg.append(x)

pos.sort(reverse=True)
neg.sort()

ans = 0

i = 0
while i + 1 < len(pos):
    ans += pos[i] * pos[i+1]
    i += 2
if i < len(pos):
    ans += pos[i]

i = 0
while i + 1 < len(neg):
    ans += neg[i] * neg[i+1]
    i += 2
if i < len(neg):
    if zeros == 0:
        ans += neg[i]

ans += ones

print(ans)'''
#8892번 팰린드롬
'''t = int(input())

for _ in range(t):
    k = int(input())
    words = [input() for _ in range(k)]
    f = False

    for i in range(k):
        for j in range(k):
            if i == j:
                continue
            s = words[i] + words[j]
            if s == s[::-1]:
                print(s)
                f = True
                break
        if f:
            break

    if not f:
        print(0)'''
#1235번 학생 번호
'''n = int(input())

l = []
arr = []

for _ in range(n):
    b = input()
    l.append(b)

for i in range(len(b) - 1, -1, -1):
    for j in range(n):
        arr.append(l[j][i:])
        if arr.count(l[j][i:]) > 1:
            arr = []
            break
    else:
        print(len(b) - i)
        break'''
#1531번 투명
'''n, m = map(int, input().split())
picture = [[0]*101 for _ in range(101)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            picture[x][y] += 1

cnt = 0
for i in range(101):
    for j in range(101):
        if picture[i][j] > m:
            cnt += 1

print(cnt)'''
#8595 히든 넘버
'''n = int(input())
word = list(input())
d = '0123456789'
ans = 0
t = 0

for i in word:
    if i in d:
        t *= 10
        t += int(i)
    else:
        ans += t
        t = 0
        
if t > 0:
    ans += t

print(ans)'''
#2960번 에라토스테네스의 체
'''n, k = map(int, input().split())
l = [True] * (n + 1)
cnt = 0
x = 0

for i in range(2, n + 1):
    if l[i]:
        for j in range(i, n + 1, i):
            if l[j]:
                l[j] = False
                cnt += 1
                if cnt == k:
                    x = j
                    break
        if x != 0:
            break

print(x)'''
#24039번 2021은 무엇이 특별할까?
'''n = int(input())
l = []

for i in range(2, 10001):
    for j in range(2, i + 1):
        if j == i:
            l.append(i)
        if i % j == 0:
            break

for x in range(len(l) - 1):
    if l[x] * l[x + 1] > n:
        print(l[x] * l[x + 1])
        break'''
#4659번 비밀번호 발음하기
'''mo = 'aeiou'
eo = 'eo'

while True:
    word = input()
    
    if word == "end":
        break
    
    has_mo = False
    mocount = 0
    jacount = 0
    acceptable = True

    if word[0] in mo:
        mocount = 1
        jacount = 0
        has_mo = True
    else:
        jacount = 1
        mocount = 0

    for i in range(1, len(word)):
        if word[i] == word[i-1] and word[i] not in eo:
            acceptable = False
            break

        if word[i] in mo:
            has_mo = True
            mocount += 1
            jacount = 0
        else:
            jacount += 1
            mocount = 0
            
        if mocount == 3 or jacount == 3:
            acceptable = False
            break

    if acceptable and has_mo:
        print("<%s> is acceptable." % word)
    else:
        print("<%s> is not acceptable." % word)'''
#10163번 색종이
'''import sys

input = sys.stdin.readline

n = int(input())
paper = [[0]*1001 for _ in range(1001)]

for k in range(1, n+1):
    x, y, w, h = map(int, input().split())
    for i in range(x, x+w):
        for j in range(y, y+h):
            paper[i][j] = k

result = [0]*(n+1)

for i in range(1001):
    for j in range(1001):
        if paper[i][j] != 0:
            result[paper[i][j]] += 1

for i in range(1, n+1):
    print(result[i])'''
#2217번 로프
'''import sys

input = sys.stdin.readline

n = int(input())
l = []
ans = 0

for _ in range(n):
    l.append(int(input()))

l.sort()

for i in range(n):
    ans = max(ans, l[i] * (n - i))

print(ans)'''
#11179 2진수 뒤집기
'''n = int(input())

n = str(bin(n)[2:])[::-1]

print(int('%s' % n, 2))'''
#14916번 거스름돈
'''def make_change(n, d):
    INF = 10**9
    c = [INF for x in range(n+2)]
    c[0] = 0 
    for j in range(1, n+1):
        for i in range(len(d)):
            if d[i] <= j and c[j-d[i]]+1 < c[j]:
                c[j] = c[j-d[i]] + 1
    return c

coins = [5, 2]

N = int(input())

num_coins = make_change(N, coins)

print(-1 if num_coins[N] == 10 ** 9 else num_coins[N])'''
#1337번 올바른 배열
'''n = int(input())
l = []
cnt = 0
cnt_l = []

for _ in range(n):
    l.append(int(input()))

l.sort()

for i in range(n):
    arr = [x for x in range(l[i], l[i]+5)]
    for j in range(n):
        if l[j] in arr:
            cnt += 1
    cnt_l.append(5 - cnt)
    cnt = 0

print(min(cnt_l))'''
#5635번 생일
'''n = int(input())
l = []
n_l = []

for _ in range(n):
    l.append(input().split())

for i in range(n):
    arr = []
    arr = [int(l[i][3]), int(l[i][2]), int(l[i][1]), l[i][0]]
    n_l.append(arr)

n_l.sort()

print(n_l[n-1][3])
print(n_l[0][3])'''
#7568번 덩치
'''n = int(input())
l = []

for _ in range(n):
    l.append(list(map(int, input().split())))

for i in range(n):
    rank = 1
    for j in range(n):
        if i == j:
            continue
        if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
            rank += 1
    print(rank, end=' ')'''
#2567번 색종이 - 2
'''import sys

input = sys.stdin.readline

n = int(input())
l = []
g = [[0]*100 for _ in range(100)]
arr = []

for __ in range(n):
    l.append(list(map(int, input().split())))

for i in range(n):
    for x in range(l[i][0], l[i][0]+10):
        for y in range(l[i][1], l[i][1]+10):
            g[x][y] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 0
for x in range(30):
    for y in range(30):
        if g[x][y] == 1:
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or ny < 0 or nx >= 30 or ny >= 30:
                    ans += 1
                elif g[nx][ny] == 0:
                    ans += 1

print(ans)'''
#1316번 그룹 단어 체커
'''n = int(input())
cnt = 0

for _ in range(n):
    word = input()
    l = [0] * 26
    arr = word[0]
    l[ord(arr) - 97] = 1
    b = True
    
    for i in range(1, len(word)):
        if word[i] != arr:
            idx = ord(word[i]) - 97
            if l[idx] == 1:
                b = False
                break
            l[idx] = 1
            arr = word[i]
    if b:
        cnt += 1

print(cnt)'''
#2669번 직각사각형 네개의 합집합의면적 구하기
'''import sys
input = sys.stdin.readline

paper = [[0]*101 for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            paper[i][j] = 1

ans = 0
for i in range(101):
    for j in range(101):
        if paper[i][j] == 1:
            ans += 1

print(ans)'''
#6159번 Costume Party
'''import sys

input = sys.stdin.readline

n, s = map(int, input().split())
l = []
cnt = 0

for _ in range(n):
    l.append(int(input()))

for i in range(n):
    for j in range(i+1,n):
        if l[i] + l[j] <= s:
            cnt += 1

print(cnt)'''
#20115번 에너지 드링크
'''n = int(input())
e_l = list(map(int, input().split()))

d = max(e_l)

e_l.remove(d)

ans = sum(e_l) / 2 + d

print(ans)'''
#백준 22993번 서든어택 3
'''n = int(input())
l = list(map(int, input().split()))

p = l.pop(0)
l.sort()

for i in range(len(l)):
    if p <= l[i]:
        print("No")
        break
    p += l[i]
else:
    print("Yes")'''
#23056번 참가자 명단
'''n, m = map(int, input().split())

c = {}
for i in range(1, n + 1):
    c[i] = []
    
while True:
    cnum, name = input().split()
    cnum = int(cnum)
    if cnum == 0:
        break
    if len(c[cnum]) == m:
        continue
    c[cnum].append(name)

for cnum in range(1, n+1, 2):
    if len(c[cnum])==0:
        continue
    c[cnum].sort(key=lambda x:(len(x),x))
    for x in c[cnum]:
        print(cnum,x)

for cnum in range(2, n+1, 2):
    if len(c[cnum])==0:
        continue
    c[cnum].sort(key=lambda x:(len(x),x))
    for x in c[cnum]:
        print(cnum,x)'''
#13022번 늑대와 올바른 단어
'''s = input()

l = ['w', 'o', 'l', 'f']
i = 0
n = len(s)
b = True

while i < n and b:
    cnt = [0, 0, 0, 0]
    for x in range(4):
        if i >= n or s[i] != l[x]:
            b = False
            break
        k = s[i]
        while i < n and s[i] == k:
            cnt[x] += 1
            i += 1
    if b and not (cnt[0] == cnt[1] == cnt[2] == cnt[3]):
        b = False

print(1 if b else 0)'''
#1393번 음하철도 구구팔
'''import math

xs, ys = map(int, input().split())
xe, ye, dx, dy = map(int, input().split())

k = math.gcd(dx, dy)
dx //= k
dy //= k

answer = (abs(xs - xe) ** 2 + abs(ys - ye) ** 2) ** 0.5
ax, ay = xe, ye

while -100 <= xe <= 100 and -100 <= ye <= 100:
    xe += dx
    ye += dy
    temp = (abs(xs - xe) ** 2 + abs(ys - ye) ** 2) ** 0.5
    if answer > temp:
        answer = temp
        ax, ay = xe, ye
    else:
        break

print(ax, ay)'''
#1697번 숨바꼭질
'''from collections import deque

def bfs(n, k):
    visited = [False] * 100001
    queue = deque([(n, 0)])
    while queue:
        current, time = queue.popleft()
        if current == k:
            return time
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))

n, k = map(int, input().split())
print(bfs(n, k))'''
#10837번 동전 게임
'''k = int(input())
c = int(input())

for i in range(c):
    m, n = map(int, input().split())
    
    if m == n:
        print(1)
    
    elif m < n:
        if n * 2 - m - k <= 1:
            print(1)
        else:
            print(0)
    elif m > n:
        if m * 2 - n - k <= 2:
            print(1)
        else:
            print(0)'''
#1270번 전쟁 - 땅따먹기
'''from collections import Counter

n = int(input())

for i in range(n):
    t = list(map(int, input().split()))
    f = t.pop(0)
    c = Counter(t)
    k = c.most_common(1)
    
    if k[0][0] * k[0][1] > f // 2:
        print(k[0][0])
    else:
        print("SYJKGW")'''
#14425번 문자열 집합
'''n, m = map(int, input().split())
s = set()
cnt = 0

for _ in range(n):
    s.add(input())

for i in range(m):
    k = input()
    if k in s:
        cnt += 1

print(cnt)'''
#1758번 알바생 강호
'''n = int(input())
l = []
tip = []
k = 1

for _ in range(n):
    l.append(int(input()))

l.sort(reverse = True)

for i in range(n):
    if l[i] - (k - 1) > 0:
        tip.append(l[i] - (k - 1))
    else:
        continue
    
    k += 1

print(sum(tip))'''
#1929번 소수 구하기
'''import sys

input = sys.stdin.readline

m, n = map(int, input().split())

def isPrime(a):
    if a < 2:
        return False
    
    for i in range(2, int(a ** 0.5)+1):
        if a % i == 0:
            return False
    
    return True

for i in range(m, n + 1):
    if isPrime(i):
        print(i)'''
#31575번 도시와 비트코인
'''n, m = map(int, input().split())
c = []

for _ in range(m):
    c.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(m)]

if c[0][0] == 0:
    print("No")
    exit()

dp[0][0] = 1

for i in range(m):
    for j in range(n):
        if c[i][j] == 0:
            continue
        if i > 0 and dp[i-1][j] == 1:
            dp[i][j] = 1
        if j > 0 and dp[i][j-1] == 1:
            dp[i][j] = 1

print("Yes" if dp[m - 1][n - 1] == 1 else "No")'''
#1158번 요세푸스 문제
'''n, k = map(int, input().split())
c = [i for i in range(1, n + 1)]
result = []
idx = 0

while c:
    idx = (idx + k - 1) % len(c)
    result.append(c.pop(idx))

print('<', end = '')
print(*result, sep=', ', end = '>')'''
#9536번 여우는 어떻게 울지?
'''t = int(input())

for __ in range(t):
    all_cry = list(input().split())
    
    while True:
        ani_cry = list(input().split())
        
        if ani_cry == ['what', 'does', 'the', 'fox', 'say?']:
            break
        
        if ani_cry[2] in all_cry:
            k = all_cry.count(ani_cry[2])
            for _ in range(k):
                all_cry.remove(ani_cry[2])
                
    print(*all_cry)'''
#3018번 캠프파이어
'''import sys

# 입력 속도를 위해 sys.stdin.readline 사용 권장
input = sys.stdin.readline

n = int(input())
t = int(input())

# [수정 1] 각 사람마다 별도의 set 객체 생성
l = [set() for _ in range(n + 1)]
s = 0 # 노래 번호 카운터

for _ in range(t):
    a = list(map(int, input().split()))
    # a[0]은 인원수, a[1:]은 참석자 리스트
    attendees = a[1:]
    
    # [수정 2] 로직 수정
    if 1 in attendees:
        # 선영이가 있으면: 새로운 노래(s)가 생성됨
        s += 1
        for person in attendees:
            l[person].add(s)
    else:
        # 선영이가 없으면: 참석자끼리 아는 노래를 공유(Union)
        union_songs = set()
        # 1. 참석자들의 모든 노래를 모음
        for person in attendees:
            union_songs.update(l[person])
        # 2. 모은 노래를 다시 참석자들에게 분배
        for person in attendees:
            l[person] = union_songs.copy() # 혹은 l[person].update(union_songs)

# 결과 출력
# 선영이(1번)가 아는 노래 개수와 같은지 확인
target_count = len(l[1])

for i in range(1, n + 1):
    if len(l[i]) == target_count:
        print(i)'''
#6186번 Best Grass
'''import sys

input = sys.stdin.readline

r, c = list(map(int, input().split()))
grass = [list(input().strip()) for _ in range(r)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution():
    clump = 0
    visit = [[0] * c for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if not visit[x][y] and grass[x][y] == '#':
                visit[x][y] = 1
                clump += 1

                for i in range(4):
                    nr, nc = x + dx[i], y + dy[i]
                    if 0 <= nr < r and 0 <= nc < c:
                        if not visit[nr][nc]:
                            visit[nr][nc] = 1

    return clump

print(solution())'''
#9375번 패션왕 신해빈
'''t = int(input())
d = {}

for k in range(t):
    d = {}
    n = int(input())
    
    for i in range(n):
        k, v = input().split()
        if v not in d:
            d[v]=[]
        d[v].append(k)
    
    s = 1
    
    for x in d:
        s *= (len(d[x]) + 1)
    
    print(s - 1)'''
#1388번 나무 장식
'''n, m = map(int, input().split())
l = []
cnt = 0

for _ in range(n):
    l.append(list(input()))

visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        cnt += 1
        visited[i][j] = True
        if l[i][j] == '-':
            x = j + 1
            while x < m and l[i][x] == '-':
                visited[i][x] = True
                x += 1
        if l[i][j] == '|':
            y = i + 1
            while y < n and l[y][j] == '|':
                visited[y][j] = True
                y += 1

print(cnt)'''
#1002번 터렛
'''t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue
    if x1 == x2 and y1 == y2 and r1 != r2:
        print(0)
        continue
    
    if ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 == abs(r1 + r2):
        print(1)
    elif ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 < abs(r1 + r2) and not ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 < abs(r1 - r2) and not ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 == abs(r1 - r2):
        print(2)
    elif ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 == abs(r1 - r2):
        print(1)
    elif ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 > abs(r1 - r2):
        print(0)
    elif ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 < abs(r1 - r2):
        print(0)'''
#1072번 게임
'''import sys

input = sys.stdin.readline

x, y = map(int, input().split())

z = int((y * 100) / x)

if z >= 99:
    print(-1)
    sys.exit()

left, right = 1, 3000000000
ans = -1

while left <= right:
    mid = (left + right) // 2
    new_z = ((y + mid) * 100) // (x + mid)

    if new_z > z:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)'''
#1913번 달팽이
'''a = int(input())

if a % 2 == 0:
    print("CY")
else:
    print("SK")'''
#15686번 치킨 배달
'''n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

c_len = len(chickens)
answer = 10**9

for mask in range(1 << c_len):
    cnt = 0
    for i in range(c_len):
        if mask & (1 << i):
            cnt += 1
    if cnt != m:
        continue

    total = 0
    for hx, hy in houses:
        dist = 10**9
        for i in range(c_len):
            if mask & (1 << i):
                cx, cy = chickens[i]
                d = abs(hx - cx) + abs(hy - cy)
                if d < dist:
                    dist = d
        total += dist

    if total < answer:
        answer = total

print(answer)'''
#1106번 호텔
'''import sys
input = sys.stdin.readline

C, N = map(int, input().split())

INF = 10**9
dp = [INF] * (C + 101)
dp[0] = 0

for _ in range(N):
    cost, people = map(int, input().split())
    for i in range(people, C + 101):
        dp[i] = min(dp[i], dp[i - people] + cost)

print(min(dp[C:]))'''
#2479번 경로 찾기
'''from collections import deque

n, k = map(int, input().split())
arr = ['0'] + [input() for _ in range(n)]
s, e = map(int, input().split())
visited = [0] * (n + 1)

visited[s] = 1
q = deque()
q.append((s, str(s)))

while q:
    num, code = q.popleft()
    
    if num == e:
        print(code)
        exit()
    
    for i in range(1, n + 1):
        cnt = 0
        if visited[i]:
            continue
        for j in range(k):
            if arr[num][j] != arr[i][j]:
                cnt += 1
            if cnt > 1:
                break
    
        if cnt == 1:
            visited[i] = 1
            q.append((i, code + ' ' + str(i)))

print(-1)'''
#2178번 미로 탐색
'''from collections import deque

n, m = map(int, input().split())
l = []

for _ in range(n):
    l.append(list(map(int, input())))

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if l[nx][ny] == 0:
                continue
            if l[nx][ny]==1:
                l[nx][ny] = l[x][y] + 1
                queue.append((nx, ny))
    
    return l[n - 1][m - 1]

print(bfs(0, 0))'''
#2667번 단지번호붙이기
'''from collections import deque

n = int(input())
l = []

for _ in range(n):
    l.append(list(map(int, input().strip())))

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((x, y))
    l[x][y] = 0
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if l[nx][ny] == 1:
                l[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt

result = []

for i in range(n):
    for j in range(n):
        if l[i][j] == 1:
            result.append(bfs(i, j))

result.sort()

print(len(result))

for r in result:
    print(r)'''
#14503번 로봇 청소기
'''n, m = map(int, input().split())
r, c, d = map(int, input().split())

room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 0

while True:
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1

    cleaned = False

    for _ in range(4):
        d = (d + 3) % 4
        nr = r + dr[d]
        nc = c + dc[d]

        if room[nr][nc] == 0:
            r, c = nr, nc
            cleaned = True
            break

    if not cleaned:
        back = (d + 2) % 4
        br = r + dr[back]
        bc = c + dc[back]

        if room[br][bc] == 1:
            break
        else:
            r, c = br, bc

print(cnt)'''
#1074 Z
'''n, r, c = map(int, input().split())
s = 0

def z(x, y, d):
    global s
    if not (x <= r < x + d and y <= c < y + d):
        s += d * d
        return
    if d == 1:
        print(s)
        exit()
    
    z(x, y, d // 2)
    z(x, y + d // 2, d // 2)
    z(x + d // 2, y, d // 2)
    z(x + d // 2, y + d // 2, d // 2)

z(0, 0, 2 ** n)'''
#8981 입력숫자
'''N = int(input())
Y = list(map(int, input().split()))

X = [0] * N

pos = 0

for value in Y:
    while X[pos] != 0:
        pos = (pos + 1) % N
    
    X[pos] = value
    
    pos = (pos + value) % N

print(N)
print(*X)'''
#1600 말이 되고픈 원숭이
'''import sys

input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(h)]
visit = [[0, 0, 0, set([(0, 0)])]]
d = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
d2 = ((1, 0), (0, 1), (-1, 0), (0, -1))
ans = float('inf')

while len(visit)>0:
    x, y, used, visited = visit.pop(0)
    if x == h - 1 and y==w-1:
        ans=min(ans,len(visited)-1)
        continue
    if used<k:
        for di in d:
            nx=x+di[0]
            ny=y+di[1]
            if 0<=nx<h and 0<=ny<w:
                if g[nx][ny]==0 and (nx,ny) not in visited:
                    visit.append([nx,ny,used+1,visited|set([(nx,ny)])])
    for di in d2:
        nx=x+di[0]
        ny=y+di[1]
        if 0<=nx<h and 0<=ny<w:
            if g[nx][ny]==0 and (nx,ny) not in visited:
                visit.append([nx,ny,used+1,visited|set([(nx,ny)])])

if ans==float('inf'):
    ans=-1
print(ans)'''
#14502 연구소
'''from collections import deque
import copy

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ans = 0

def bfs():
    global ans
    queue = deque()
    t_graph = copy.deepcopy(graph)

    for i in range(n):
        for j in range(m):
            if t_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if t_graph[nx][ny] == 0:
                t_graph[nx][ny] = 2
                queue.append((nx, ny))

    cnt = 0
    for i in range(n):
        cnt += t_graph[i].count(0)

    ans = max(ans, cnt)

def wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt + 1)
                graph[i][j] = 0

wall(0)

print(ans)'''
#2624번 동전 바꿔주기
'''t = int(input())
k = int(input())
coins = [list(map(int, input().split())) for _ in range(k)]
result = [0] * (t + 1)
result[0] = 1

for p, n in coins:
    for x in range(t, 0, -1):
        for i in range(1, n + 1):
            ans = x - (p * i)
            if ans >= 0:
                result[x] += result[ans]

print(result[t])'''
#2638번 치즈
'''from copy import deepcopy

n, m = map(int, input().split())
cheese = [[0 for _ in range(m + 2)]]

for i in range(n):
    cheese.append([0] + list(map(int, input().split())) + [0])
cheese.append([0 for _ in range(m + 2)])

t = 0
d = ((-1, 0), (1, 0), (0, -1), (0, 1))

while True:
    temp = deepcopy(cheese)
    melt = True
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if cheese[i][j] == 1:
                s = 0
                for di in d:
                    x = i + di[0]
                    y = j + di[1]
                    if cheese[x][y] == 0:
                        s += 1
                if s >= 2:
                    temp[i][j] = 0
                    melt = False
    if melt:
        break
    
    cheese = deepcopy(temp)
    t += 1

print(t)'''
#4256 트리
'''def sol(pre, ino):
    if not pre:
        return

    root = pre[0]
    idx = ino.index(root)

    sol(pre[1:1+idx], ino[:idx])
    sol(pre[1+idx:], ino[idx+1:])
    print(root, end=' ')

t = int(input())

for _ in range(t):
    n = int(input())
    preor = list(map(int, input().split()))
    inor = list(map(int, input().split()))
    
    sol(preor, inor)
    print()'''
#34201번 거울
'''n, s = map(int, input().split())
m = [0] + list(map(int, input().split()))

a, b = 1, n
k = n % 2

while a <= b:
    if k == 1:
        s = 2 * m[b] - s
        b -= 1
    else:
        s = 2 * m[a] - s
        a += 1
    
    k = 1 - k

print(s)'''
#32069번 가로등
'''import sys
from collections import deque

input = sys.stdin.readline

l, n, k = map(int, input().split())
a = list(map(int, input().split()))
lux = []
visit = {}

for x in a:
    lux.append(0)
    visit[x] = 0

q = deque(a)
c = 0

while len(visit) > 0:
    temp = q.popleft()
    c += 1
    if c == k:
        break
    if temp > 0 and temp - 1 not in visit:
        lux.append(visit[temp] + 1)
        visit[temp - 1] = visit[temp] + 1
        q.append(temp - 1)
    if temp < l and temp + 1 not in visit:
        lux.append(visit[temp] + 1)
        visit[temp + 1] = visit[temp] + 1
        q.append(temp + 1)

ans = 0

for i in range(k):
    print(lux[i])'''
#27850번 Stamp Grid
'''t = int(input())

for _ in range(t):
    input()
    
    n = int(input())
    grid = [list(input()) for _ in range(n)]
    
    k = int(input())
    stamp = [input() for _ in range(k)]
    ans = [['.' for _ in range(n)] for _ in range(n)]
    
    for r in range(4):
        for i in range(n - k + 1):
            for j in range(n - k + 1):
                if all(grid[i + a][j + b] == '*' or stamp[a][b] == '.' for a in range(k) for b in range(k)):
                    for a in range(k):
                        for b in range(k):
                            if stamp[a][b] == '*':
                                ans[i + a][j + b] = '*'
        stamp = [[stamp[j][k - 1 - i] for j in range(k)] for i in range(k)]
        
    print("YES" if grid == ans else "NO")'''
'''n = int(input())

ans = [0] * 10
len_n = len(str(n))
power = 1

while power <= n:
    q = n // (power * 10)
    r = n % (power * 10)
    cur_digit = (n // power) % 10
    
    for d in range(10):
        ans[d] += q * power
    
    for d in range(1, cur_digit):
        ans[d] += power
    ans[cur_digit] += r - power + 1 if cur_digit > 0 else r + 1
    
    if cur_digit == 0:
        ans[0] -= power
    
    power *= 10

print(*ans)'''
#11403번 경로 찾기
'''import sys

input = sys.stdin.readline

n = int(input().strip())
l = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        if l[i][k]:
            for j in range(n):
                if l[k][j]:
                    l[i][j] = 1

for asdf in l:
    print(' '.join(map(str, asdf)))'''
#11562번 백양로 브레이크
'''n, m = map(int, input().split())
INF = float("inf")

board = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    board[i][i] = 0

for _ in range(m):
    v1, v2, f = map(int, input().split())
    board[v1][v2] = 0
    if f == 0:
        board[v2][v1] = 1
    else:
        board[v2][v1] = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if board[j][k] > board[j][i] + board[i][k]:
                board[j][k] = board[j][i] + board[i][k]

for _ in range(int(input())):
    s, e = map(int, input().split())
    print(board[s][e])'''
#17390번 이건 꼭 풀어야 해!
'''import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

prefix = [0] * (n + 1)

for i in range(n):
    prefix[i + 1] = prefix[i] + arr[i]

for _ in range(q):
    l, r = map(int, input().split())
    print(prefix[r] - prefix[l - 1])'''
#18353번 병사 배치하기
'''n = int(input())
soldiers = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if soldiers[i] < soldiers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))'''
#14627번 파닭파닭
'''import sys
input = sys.stdin.readline

S, C = map(int, input().split())
arr = [int(input()) for _ in range(S)]

left = 1
right = max(arr)
answer = 0

while left <= right:
    mid = (left + right) // 2
    
    total = 0
    for length in arr:
        total += length // mid
    
    if total >= C:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

total_length = sum(arr)
used = answer * C

print(total_length - used)'''
#25212 조각 케이크
'''from itertools import combinations

def count_cake_combinations(n, cake_sizes):
    cake_fractions = [1 / c for c in cake_sizes]
    count = 0
    for r in range(1, n + 1):
        for subset in combinations(cake_fractions, r):
            total = sum(subset)
            if 0.99 <= total <= 1.01:
                count += 1
    return count

n = int(input())
cake_sizes = list(map(int, input().split()))
print(count_cake_combinations(n, cake_sizes))'''
#16568번 엔비스카의 영혼
'''from collections import deque
import sys

input = sys.stdin.readline

n, a, b = map(int, input().split())
dp = [float("inf")] * 1000001
dp[n] = 0

for i in range(n, -1, -1):
    if i - 1 >= 0:
        dp[i - 1] = min(dp[i - 1], dp[i] + 1)
    if i - a - 1 >= 0:
        dp[i - a - 1] = min(dp[i - a - 1], dp[i] + 1)
    if i - b - 1 >= 0:
        dp[i - b - 1] = min(dp[i - b - 1], dp[i] + 1) 

print(dp[0])'''
#15925번 욱제는 정치쟁이야!!
'''import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        arr[i][j] = row[j - 1]

while True:
    changed = False
    for i in range(1, n + 1):
        cnt = sum(1 for j in range(1, n + 1) if arr[i][j] == x)
        if cnt > n // 2:
            for j in range(1, n + 1):
                if arr[i][j] != x:
                    arr[i][j] = x
                    changed = True
        cnt = sum(1 for j in range(1, n + 1) if arr[j][i] == x)
        if cnt > n // 2:
            for j in range(1, n + 1):
                if arr[j][i] != x:
                    arr[j][i] = x
                    changed = True
    
    if not changed:
        break

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] != x:
            print(0)
            sys.exit()

print(1)'''
#28066번 타노스는 요세푸스가 밉다
'''from collections import deque

N, K = map(int, input().split())
squirrel = deque(range(1, N + 1))

while len(squirrel) != 1:
    squirrel.rotate(-1)
    for i in range(K - 1):
        squirrel.popleft()
        if len(squirrel) == 1:
            break

print(*squirrel)'''
#11123번 양 한마리... 양 두마리...
'''import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == '#':
                grid[nx][ny] = '.'
                stack.append((nx, ny))

for _ in range(T):
    h, w = map(int, input().split())
    grid = [list(input().strip()) for _ in range(h)]
    
    count = 0
    
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#':
                grid[i][j] = '.'
                dfs(i, j)
                count += 1
    
    print(count)'''
#31848번 엉성한 도토리 분류기
'''def search(data, dotori_qty):
    lo = 0
    hi = len(data) - 1

    while lo < hi:
        mid = (lo + hi) // 2
        if data[mid][0] >= dotori_qty:
            hi = mid
        else:
            lo = mid + 1

    return lo

def get_input():
    hole_cnt = int(input())
    hole_qty_list = [(int(qty) + idx, idx) for idx, qty in enumerate(input().split())]
    hole_qty = [hole_qty_list[0]]

    dotori_cnt = int(input())
    dotori_qty = list(map(int, input().split()))

    for qty in hole_qty_list[1:]:
        if hole_qty[-1][0] < qty[0]:
            hole_qty.append(qty)

    return hole_cnt, hole_qty, dotori_cnt, dotori_qty


if __name__ == '__main__':
    result = []

    hole_cnt, hole_qty, dotori_cnt, dotori_qty = get_input()

    for qty in dotori_qty:
        result.append(str(hole_qty[search(hole_qty, qty)][1] + 1))

    print(' '.join(result))'''
#2890번 카약
'''import sys

input = sys.stdin.readline

r, c = map(int, input().split())
history_dict = dict(zip(range(1, 10), [0] * 9))

for i in range(1, r + 1):
    line = sys.stdin.readline().rstrip()

    if line.count('.') == c - 2:
        continue
    
    kayak_distance = 0

    for char in line[1:-1]:
        if char.isdigit():
            history_dict[int(char)] = kayak_distance
            break
        
        kayak_distance += 1

history_list = sorted(history_dict.items(), key=lambda x: -x[1])

current_rank = 1
before = -1

rank_list = [0] * (9 + 1)

for kayak, distance in history_list:
    if before < 0:
        before = distance

    if before != distance:
        current_rank += 1
    
    rank_list[kayak] = current_rank
    before = distance

for rank in rank_list[1:]:
    print(rank)'''
#20002번 사과나무
'''import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ps = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        ps[i][j] = (arr[i-1][j-1] + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1])

answer = -10**18

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(n):
            ni = i + k
            nj = j + k
            if ni > n or nj > n:
                break
            total = (ps[ni][nj] - ps[i-1][nj] - ps[ni][j-1] + ps[i-1][j-1])
            answer = max(answer, total)

print(answer)'''
#1245번 농장 관리
'''import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] > 0 and not visited[i][j]:
            q = deque()
            q.append((i, j))
            visited[i][j] = True
            height = graph[i][j]
            is_peak = True

            while q:
                x, y = q.popleft()

                for d in range(8):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < n and 0 <= ny < m:
                        if graph[nx][ny] > height:
                            is_peak = False
                        if graph[nx][ny] == height and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))

            if is_peak:
                answer += 1

print(answer)'''
#27210번 신을 모시는 사당
'''import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

a = [1 if x == 1 else -1 for x in arr]

dp_max = [0] * n
dp_min = [0] * n

dp_max[0] = a[0]
dp_min[0] = a[0]

answer = abs(a[0])

for i in range(1, n):
    dp_max[i] = max(a[i], dp_max[i-1] + a[i])
    dp_min[i] = min(a[i], dp_min[i-1] + a[i])
    answer = max(answer, dp_max[i], -dp_min[i])

print(answer)'''
#33679번 세기의 대결
'''def get_max_score(bullets):
    n = len(bullets)
    best = 0

    for start in range(n):
        seq = [bullets[(start + i) % n] for i in range(n)]

        dp = [1] * n
        local_max = 0

        for i in range(n):
            for j in range(i):
                if seq[j] < seq[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            local_max = max(local_max, dp[i])

        best = max(best, local_max)

    return best


def main():
    N = int(input())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    scoreA = get_max_score(A)
    scoreB = get_max_score(B)

    if scoreA > scoreB:
        print("YJ win!")
    elif scoreA < scoreB:
        print("HG win!")
    else:
        print("Both win!")


if __name__ == "__main__":
    main()'''
#20003번 거스름돈이 싫어요
'''import fractions
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return a*b//gcd(a,b)

n=int(input())
g,l=0,1
for i in range(n):
    a,b=map(int,input().split())
    temp=fractions.Fraction(a,b)
    g=gcd(g,temp.numerator)
    l=lcm(l,temp.denominator)

print(g,l)'''
#2747번 피보나치 수
'''n = int(input())
l = [0, 1]

for i in range(n):
    l.append(sum(l[i:]))

print(l[n])'''
#9095번 1, 2, 3 더하기
'''t = int(input())

for _ in range(t):
    n = int(input())
    l = [1, 2, 4]
    if n > 3:
        for i in range(n - 2):
            l.append(sum(l[i:i + 3]))
    print(l[n - 1])'''
#11726번 2×n 타일링
'''n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[n])'''
#11727번 2xn 타일링 2
'''n = int(input())
dp = [0] * (n + 1)

dp[1] = 1

if n > 1:
    for i in range(2, n + 1):
        if i % 2:
            dp[i] = dp[i-1] * 2 - 1
        else:
            dp[i] = dp[i-1] * 2 + 1

print(dp[n] % 10007)'''
#17626번 Four Squares
'''n = int(input())
count = 0

DP = [0] * (n + 1)

k = 1
while k**2 <= n:
    DP[k**2] = 1
    k += 1

for i in range(1, n + 1):
    if DP[i] != 0:
        continue
    j = 1
    while j*j <= i:
        if DP[i] == 0:
            DP[i] = DP[j*j] + DP[i - j*j]
        else:
            DP[i] = min(DP[i], DP[j*j] + DP[i - j*j])
        j += 1
print(DP[n])'''
#2156번 포도주 시식
'''a=int(input())
l=[int(input()) for i in range(a)]
dp=[0]*(a+1)

if a==0:
    print(0)
    exit()
elif a==1:
    print(l[0])
    exit()
elif a==2:
    print(l[0]+l[1])
    exit()

dp[0]=l[0]
dp[1]=l[0]+l[1]
dp[2]=max(l[0]+l[1],l[1]+l[2],l[0]+l[2])

for i in range(3,a):
    dp[i]=max(dp[i-1],dp[i-2]+l[i],dp[i-3]+l[i-1]+l[i])
print(dp[a-1])'''
#9465번 스티커
'''import sys

input = sys.stdin.readline

tc = int(input().strip())

for _ in range(tc):
    n = int(input().strip())
    
    arr = []
    arr.append(list(map(int,input().strip().split())))
    arr.append(list(map(int, input().strip().split())))
    sum = list([0] * n for _ in range(2))
    sum[0][0] = arr[0][0]
    sum[1][0] = arr[1][0]
    
    result = max(sum[0][0], sum[1][0])
    if n > 1:
        sum[0][1] = sum[1][0] + arr[0][1]
        sum[1][1] = sum[0][0] + arr[1][1]
        result = max(sum[0][1], sum[1][1], result)
        for i in range(2, n):
            sum[0][i] = max(sum[0][i-2], sum[1][i-2], sum[1][i-1]) + arr[0][i]
            sum[1][i] = max(sum[0][i-2], sum[1][i-2], sum[0][i-1]) + arr[1][i]
            result = max(sum[0][i], sum[1][i], result)
    print(result)'''
#11053번 가장 긴 증가하는 부분 수열
'''n = int(input())
arr = list(map(int, input().split()))
lis_len = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i] and lis_len[j] >= lis_len[i]:
            lis_len[i] = lis_len[j] + 1

ans = max(lis_len) if lis_len else 0

print(ans)'''
#2133번 타일 채우기
'''MAXN = 30
arr = [0] * (MAXN + 1)

n = int(input())
if n % 2 != 0:
    print(0)
    exit()

arr[0] = 1
arr[2] = 3
for i in range(4, 31, 2):
    arr[i] += arr[i-2] * 3
    for j in range(4, i+1):
        arr[i] += arr[i-j] * 2

print(arr[n])'''
#
'''MAXN = 30
arr = [0] * (MAXN + 1)

n = int(input())
if n % 2 != 0:
    print(0)
    exit()

arr[0] = 1
arr[2] = 3
for i in range(4, 31, 2):
    arr[i] += arr[i-2] * 3
    for j in range(4, i+1):
        arr[i] += arr[i-j] * 2

print(arr[n])'''
#25943번 양팔 저울
'''W = [100, 50, 20, 10, 5, 2, 1]

N = int(input())
P = list(map(int, input().split()))
left, right = P[0], P[1]

for i in range(2, N) :
    if left == right :
        left += P[i]
    else :
        if left < right :
            left += P[i]
        elif left > right :
            right += P[i]

tmp = abs(left - right)

if tmp == 0 :
    print(0)
else :
    cnt = 0
    for w in W :
        if (tmp // w) != 0 :
            cnt += tmp // w
            tmp = tmp % w
    print(cnt)'''
#25287번 순열 정렬
'''def main():
    import sys
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        N = int(input())
        v = list(map(int, input().split()))
        prev = min(v[0], N - v[0] + 1)
        flag = True
        for i in range(1, N):
            mini = min(v[i], N - v[i] + 1)
            maxi = max(v[i], N - v[i] + 1)
            if prev <= mini:
                prev = mini
            elif mini < prev <= maxi:
                prev = maxi
            else:
                flag = False
                break
        print("YES" if flag else "NO")

if __name__ == "__main__":
    main()'''
#18310번 안테나
'''N = int(input())
a = list(map(int, input().split()))
a.sort()

print(a[(N - 1) // 2])'''
#2597번 줄자접기
'''N = float(input())
points = [list(map(float, input().split())) for _ in range(3)]

for i in range(3):
    if points[i][0] > points[i][1]:
        points[i][0], points[i][1] = points[i][1], points[i][0]

for i in range(3):
    if points[i][0] == points[i][1]:
        continue
    mid = (points[i][1] + points[i][0]) / 2.0
    if mid < N - mid:
        for j in range(i + 1, 3):
            if points[j][0] < mid:
                points[j][0] = mid - points[j][0]
            else:
                points[j][0] -= mid

            if points[j][1] < mid:
                points[j][1] = mid - points[j][1]
            else:
                points[j][1] -= mid

            if points[j][0] > points[j][1]:
                points[j][0], points[j][1] = points[j][1], points[j][0]
        N = N - mid
    else:
        for j in range(i + 1, 3):
            if mid < points[j][0]:
                points[j][0] = mid - (points[j][0] - mid)
            if mid < points[j][1]:
                points[j][1] = mid - (points[j][1] - mid)

            if points[j][0] > points[j][1]:
                points[j][0], points[j][1] = points[j][1], points[j][0]
        N = mid

print(f"{N:.1f}")'''
#11501번 주식
'''t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    coming = [-1] * n
    future_max = -1

    for i in range(n - 1, -1, -1):
        coming[i] = future_max
        if arr[i] > future_max:
            future_max = arr[i]

    ans = 0
    for i in range(n):
        if arr[i] < coming[i]:
            ans += coming[i] - arr[i]

    print(ans)'''
#1946번 신입 사원
'''t = int(input())

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

    print(ans)'''
#21758번 꿀 따기
'''n = int(input())
h = list(map(int, input().split()))

s = [0]*n
s[0] = h[0]
for i in range(1, n):
    s[i] = s[i-1] + h[i]

ans = 0

for i in range(1, n-1):
    ans = max(ans, (s[n-1]-s[0]-h[i]) + (s[n-1]-s[i]))
    ans = max(ans, (s[n-2]-h[i]) + s[i-1])
    ans = max(ans, (s[i]-s[0]) + (s[n-2]-s[i-1]))

print(ans)'''
#코드업 4021번 홀수의 합 구하기
'''l = list(map(int, input().split()))
arr = []

for i in l:
    if i % 2 == 1:
        arr.append(i)

print(sum(arr) if arr != [] else -1)'''
#코드업 4026번 중앙 값
'''numbers = list(map(int, input().split()))

numbers.sort()

print(numbers[2])'''
