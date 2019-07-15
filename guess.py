# Ben's number guessing game

import random

print("Welcome. What is your name?")
playerName = input()

print("")
print("Hi " + playerName + "!")

secretNumber = random.randint(1, 20)

# Loop for multiple guesses
for guessCount in range(10):
	
	guessLeft = str(9 - guessCount)

	# Check for valid input
	validInput = False
	print("")
	print("Choose a number between 1 and 20:")
	while not validInput:
		guess = input()
		guessNum = int(guess)
		
		# Ben's error checking
		if(guessNum < 1) or (guessNum > 20):
			print("Numbers must be between 1 and 20. Try again:")
		else:
			validInput = True

	#print("")
	#print("You guessed " + guess)
	# print("The real number is " + str(secretNumber))

	# Ben's good idea:
	#  Make the game respond with warmer or colder

	if(guessNum < secretNumber):
		print("Wrong! Your guess is too low! You have " + guessLeft + " more turns, try again.")
	elif(guessNum > secretNumber):
		print('Wrong! Your guess is too high! You have ' + guessLeft + ' more turns, try again.')
	else:
		print("")
		print("Congratulations " + playerName + "! You guessed right!")
		break
