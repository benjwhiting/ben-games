# Ben's number guessing game

import random

print("Welcome. What is your name?")
playerName = input()

print("")
print("Hi " + playerName + "!")

secretNumber = random.randint(1, 20)

# Loop for multiple guesses
for guessCount in range(10):
	
	guessLeft = 9 - guessCount
	triesTaken = 10 - guessLeft

	# Check for valid input
	validInput = False
	print("")
	print("Choose a number between 1 and 20:")
	while not validInput:
		guessNum = None
		guess = input()
		try:
			guessNum = int(guess)
		except:
			pass

		#check whether guessNum is an integer
		if isinstance(guessNum, int):

			# Ben's error checking
			if(guessNum < 1) or (guessNum > 20):
				print("Numbers must be between 1 and 20. Try again:")
			else:
				validInput = True

		else:
			print("Input must be a number between 1 and 20. Try again:")

	#print("")
	#print("You guessed " + guess)
	# print("The real number is " + str(secretNumber))

	# Ben's good idea:
	#  Make the game respond with warmer or colder

	if(guessNum < secretNumber):
		print("Wrong! Your guess is too low! You have " + str(guessLeft) + " more turns, try again.")
	elif(guessNum > secretNumber):
		print('Wrong! Your guess is too high! You have ' + str(guessLeft) + ' more turns, try again.')
	else:
		print("")
		print("Congratulations " + playerName + "! You guessed right, it took you " + str(triesTaken) + " tries.\n")
		break
