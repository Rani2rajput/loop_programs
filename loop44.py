i=0
num=int(input("enter number"))
while num>0:
	i=i*10+num%10
	num=num//10
print("reverse num",i)