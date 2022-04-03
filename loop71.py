n=int(input("enter num"))
i=1
c1=0
while i<=n:
	j=1
	c=0
	while j<=i:
		if i%j==0:
			c=c+1
		j=j+1
	if c==2:
		c1=c1+1
	i=i+1
print(c1)