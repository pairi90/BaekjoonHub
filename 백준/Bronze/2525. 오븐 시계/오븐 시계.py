h,m = map(int, input().split())
t = int(input())

finish = h*60+m+t
if finish < 1440:
	print(finish//60, finish%60)
else:
	print((finish)//60-24, (finish-60)%60)