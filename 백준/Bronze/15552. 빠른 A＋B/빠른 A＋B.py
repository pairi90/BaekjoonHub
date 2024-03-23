import sys

T = int(input()) 
for i in range(T):
    A,B = map(int, sys.stdin.readline().rstrip().split())
    # stdin : standard input
    # rstrip() : 오른쪽 공백 제거 -> sys.stdin.readline() 결과의 개행 문자(\n) 제거
    print(A+B)