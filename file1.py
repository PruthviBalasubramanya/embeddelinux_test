import sys
count=0
x=sys.argv[1]
with open('ip.txt') as file:
	lines = file.readlines()
for y in lines:
	y=y.split('\n')
	if x == y[0]:
		count=count+1
		print("IP is present",count,"times")
		break
	else:
		print("IP not found")
