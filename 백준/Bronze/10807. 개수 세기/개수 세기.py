n = int(input()) # 정수의 개수를 받음
li = list(map(int, input().split())) # 정수가 공백으로 구분된 줄을 받음
v = int(input()) # 찾으려고 하는 정수를 받음

cnt = 0
for i in range(n):
    if li[i] == v:
        cnt += 1
    else:
        pass
print(cnt)