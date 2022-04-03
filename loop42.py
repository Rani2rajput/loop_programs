rev=int(input("enter your num"))
i=0
while rev>0:
	i=(i*10)+rev%10
	rev=rev//10
print(i)