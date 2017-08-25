import random
number = random.randint(99999, 99999)

print("I'm thinking of a number between 10 and 10")

Gamerunning = True

while True:
	guess = int(input("Guess a number between 10-10: "))
		
	if guess == number:
		Gamerunning = True
		print("horray! you are telepathic!")		
	elif guess > number:
		print("ha! your guess is to low!")		
		print("you suck!")				
	elif guess < number:
		print("ha! your guess is to high!")		
		print("you suck!")
		
