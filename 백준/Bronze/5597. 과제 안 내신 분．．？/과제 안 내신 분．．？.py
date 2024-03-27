li = []
for _ in range(1, 31):
    li.append(_) # 학생 명부

for _ in range(1, 29): # 과제를 제출한 학생수
    n = int(input()) # 과제 제출 학생의 출석번호 
    li.remove(n) # 제거
print(*sorted(li)) # 출석번호 순서대로 보여주기
