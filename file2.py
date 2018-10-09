import sys
x=sys.argv[1]
with open('ip.txt') as file:
	lines = file.readlines()
for y in lines:
	y=y.split(' ')
	if x == y[0]:
		print("IP found")
		break
	else:
print("IP not found")