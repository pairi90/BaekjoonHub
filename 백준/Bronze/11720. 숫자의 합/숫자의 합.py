n = int(input())
str = input()

sum = 0
for s in str:
    if int(s) > 0:
        sum += int(s)
    else:
        pass
print(sum)