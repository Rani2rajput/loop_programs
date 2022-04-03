a=int(input('enter'))
i=1
count=0
while i<a:
	j=1
	b=0
	while j<=i:
		if i%j==0:
			b=b+1
		j=j+1
	if b==2:
		count+=1
		print(count,'.','prime',i)
	i=i+1