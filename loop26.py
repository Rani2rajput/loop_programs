print("wellcome to the guessing game")
import random
n=random. randint(1,10)
count=0
while n!="guess":
	if count==3:
		print("your are lost the game")
		break
	guess=int(input("enter your guess num"))
	if n>guess:
		print("your high in the game")
	elif n<guess:
		print("your low in the game")
	else:
		print("your guess is write your won®")
	count+=1