i=int(input("enter your num"))
p=0
x=i
while i>0:
	p=p*10+i%10
	i=i//10
if (x==p):
	print("palindrome",p)
else:
	print("non palindrome")