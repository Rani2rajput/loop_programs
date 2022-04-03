i=1
num=5
while i<=5:
	guess=int(input("enter your guess num"))
	if guess<num:
		print("your guess is small")
	elif guess>num:
		print("your guess is big")
	elif guess==num:
		print("your won")
		break
	i=i+1