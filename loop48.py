num=int(input("enter your num::"))
sum=0
a=1
while a<num:
	if num%a==0:
		sum=sum+a
	a=a+1
if num==a:
	print("perfect num")
else:
	print("not perfect")