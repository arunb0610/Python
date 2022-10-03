number = 23
while True :
	guess = int(input("Enter an Integer :"))
	if guess == number:
		print("Congratulations you guessed it!")
		break:
	elif guess<number:
		print("No!It is little higher than that.")
	else:
		print("No!it is lower than that")
print("Done")
