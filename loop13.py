num=int(input("enter your prime num"))
i=1
count=0
while i<=num:
	if num%i==0:
		count=count+1
	i=i+1
if count==2:
	print(num, "prime num")
else:
	print(num,"composite num")