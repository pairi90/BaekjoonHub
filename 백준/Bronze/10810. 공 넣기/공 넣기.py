n,m = map(int, input().split())

li = []
for _ in range(n):
    li.append(0) # 원소 n개가 모두 0인 리스트 생성, li = [0] * N

for _ in range(m):
    i,j,k=map(int, input().split())
    for _ in range(i-1, j): # i부터 j까지 반복
        li[_] = k
print(*li) # 리스트의 내용을 대괄호 없이 한번에 출력 가능 