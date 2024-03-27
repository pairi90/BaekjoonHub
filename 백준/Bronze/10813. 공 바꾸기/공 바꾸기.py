n,m = map(int, input().split())

li = []
for _ in range(1, n+1): # 1~n까지의 번호가 적힌 리스트
    li.append(_)

for _ in range(m):
    i,j=map(int, input().split())
    li[i-1], li[j-1] = li[j-1], li[i-1] # 스와이프 
    
print(*li)