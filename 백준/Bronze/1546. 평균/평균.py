n = int(input())
li = list(map(int, input().split()))
m = max(li)

for _ in range(n):
    li[_] = li[_]/m*100
print(sum(li)/n)