num=int(input("enter your product num"))
i=1
while num>0:
	i=i*(num%10)
	num=num//10
print(i)