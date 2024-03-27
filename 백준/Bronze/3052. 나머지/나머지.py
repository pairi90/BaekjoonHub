li=[]
for _ in range(1, 11):
    n = int(input())
    li.append(n%42)
print(len(set(li)))