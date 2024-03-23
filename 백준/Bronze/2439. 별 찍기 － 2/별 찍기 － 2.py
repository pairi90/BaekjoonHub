n = int(input())

for i in range(1, n+1):
    a = '*'*i
    print(a.rjust(n)) # n의 자리수를 a로 오른쪽에서부터 채우기