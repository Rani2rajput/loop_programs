num=int(input("enter your num"))
i=0
while num>0:
	a=num%10
	num=num//10
	if a==0:
		 i=i+1
if i>=1:
	print("duck")
else:
	print("not duck number")