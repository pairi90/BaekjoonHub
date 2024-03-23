tot = int(input())
n = int(input())

result = 0
for i in range(0, n):
    A,B = map(int, input().split())
    price = A*B
    result += price
if tot == result:
    print('Yes')
else:
    print('No')