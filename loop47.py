num=int(input("enter your number"))
sum=0
a=num
while num>0:
	r=num%10
	sum=sum+r
	num=num//10
if a%sum==0:
	print("harshad num")
else:
	print("not harshad num")