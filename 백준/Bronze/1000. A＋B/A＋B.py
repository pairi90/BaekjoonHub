# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# input().split() : 문자열('A B')를 입력으로 받아서 공백을 기준으로 구분하여 리스트 생성
# map() : 해당 리스트의 원소를 받아 int() 함수 적용

A,B = map(int, input().split())
print(A+B)