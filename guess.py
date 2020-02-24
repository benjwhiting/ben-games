# Ben's number guessing game

import random

print("Welcome. What is your name?")
playerName = input()

print("")
print("Hi " + playerName + "!")

guessNumber = 10
maxNumber = 20
secretNumber = random.randint(1, maxNumber)
#secretNumber = 15

#
# ## ADVANCED: Ask whether they want to play again

# Loop for multiple guesses
for i in range(guessNumber):

	guessCount = i + 1  

	guessLeft = guessNumber - guessCount
	triesTaken = guessNumber - guessLeft

	# Check for valid input
	validInput = False
	print("")
	#print("Choose a number between 1 and 20:")
	print("Choose a number between 1 and " + str(maxNumber) + ":")
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
			if(guessNum < 1) or (guessNum > maxNumber):
				#print("Numbers must be between 1 and 20. Try again:")
				print("Numbers must be between 1 and " + str(maxNumber) + ". Try again:")
			else:
				validInput = True

		else:
#			print("Input must be a integer between 1 and 20. Try again:")
			print("Input must be a integer between 1 and " + str(maxNumber) + ". Try again:")

	#print("")
	#print("You guessed " + guess)
	# print("The real number is " + str(secretNumber))

	if guessLeft == 1:
		turns = "turn"
	else:
		turns = "turns"

	# if it's the first turn, then do high or low
	# any turn after that is warmer or colder

	if (guessCount == 1):
		closeNew = abs(guessNum - secretNumber)
		if(guessNum < secretNumber):
			print("Wrong! Your guess is too low! You have " + str(guessLeft) + " more turns, try again.")
		elif(guessNum > secretNumber):
			print('Wrong! Your guess is too high! You have ' + str(guessLeft) + ' more turns, try again.')
		else:
			print("No way, " + playerName + "! You guessed it on the first try! \n")
			break
	elif (guessCount < guessNumber):
		closeOld = closeNew
		closeNew = abs(guessNum - secretNumber)
		warmer = closeNew < closeOld
		colder = closeNew > closeOld
		if (closeNew == 0):
			print("Congratulations " + playerName + "! You guessed right, it took you " + str(triesTaken) + " tries.\n")
			break	
		elif (warmer):
			print("You are getting warmer. You have " + str(guessLeft) + " more " + turns + ", try again.")
		elif (colder):	
			print("You are getting colder. You have " + str(guessLeft) + " more " + turns + ", try again.")
	else:
		if (guessNum == secretNumber):
			print("Congratulations " + playerName + "! You guessed right, it took you " + str(triesTaken) + " tries.\n")
			break				
		else:
			print('Game over! The real number was ' + str(secretNumber) + '.\n')
