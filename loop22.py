i=1
sum=0
while i<=11:
	num=int(input("enter your num"))
	sum=sum+num
	i=i+1
avg=sum//11
print(avg)
if avg%5==0:
	print("divisible")
else:
	print("not divisible")