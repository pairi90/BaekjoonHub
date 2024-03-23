import sys

n,x = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if li[i] < x:
        print(li[i], end=' ')