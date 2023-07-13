import random
import easygui

def initialize_game():
    guessNumber = 10
    maxNumber = 20
    secretNumber = random.randint(1, maxNumber)

    return [guessNumber, maxNumber, secretNumber]


def play_game(playerName, guessNumber, maxNumber, secretNumber):
    response = ""

    # Add window response
    response += "Hi " + playerName + "!"

    for i in range(guessNumber):
        guessCount = i + 1
        guessLeft = guessNumber - guessCount
        triesTaken = guessNumber - guessLeft
        turns = "turns" if guessLeft != 1 else "turn"

        # Check for valid input
        validInput = False
        while not validInput:
            guessNum = easygui.integerbox("Choose a number between 1 and " + str(maxNumber) + ":")
            if guessNum is not None:
                validInput = True

        response += "Guess #" + str(guessCount) + ": " + str(guessNum) + "\n"
        if guessCount == 1:
            closeNew = abs(guessNum - secretNumber)
            if guessNum < secretNumber:
                response += "Your guess is too low! You have " + str(guessLeft) + " more " + str(turns) + ".\n"
            elif guessNum > secretNumber:
                response += 'Your guess is too high! You have ' + str(guessLeft) + " more " + str(turns) + ".\n"
            else:
                response += "No way, " + playerName + "! You guessed it on the first try! \n"
                break
        elif guessCount < guessNumber:
            closeOld = closeNew
            closeNew = abs(guessNum - secretNumber)
            warmer: bool = closeNew < closeOld
            colder = closeNew > closeOld
            if closeNew == 0:
                response += "You win " + playerName + f"! It took you {triesTaken} {turns}\n"
                break
            elif warmer:
                response += "You are getting warmer. You have " + str(guessLeft) + " more " + str(turns)
            elif colder:
                response += "You are getting colder. You have " + str(guessLeft) + " more " + str(turns)
        else:
            if guessNum == secretNumber:
                response += "You win " + playerName + "! It took you " + str(triesTaken) + " tries.\n"
                break
            else:
                response += 'Game over! The real number was ' + str(secretNumber) + '.\n'

        easygui.msgbox(response)


def main():
    playerName = easygui.enterbox("Welcome. What is your name?")

    guessNumber, maxNumber, secretNumber = initialize_game()

    play_game(playerName, guessNumber, maxNumber, secretNumber)


if __name__ == "__main__":
    main()
import random
import easygui

def initialize_game():
    guessNumber = 10
    maxNumber = 20
    secretNumber = random.randint(1, maxNumber)

    return [guessNumber, maxNumber, secretNumber]


def play_game(playerName, guessNumber, maxNumber, secretNumber):
    response = ""

    # Add window response
    response += "Hi " + playerName + "!"

    for i in range(guessNumber):
        guessCount = i + 1
        guessLeft = guessNumber - guessCount
        triesTaken = guessNumber - guessLeft
        turns = "turns" if guessLeft != 1 else "turn"

        # Check for valid input
        validInput = False
        while not validInput:
            guessNum = easygui.integerbox("Choose a number between 1 and " + str(maxNumber) + ":")
            if guessNum is not None:
                validInput = True

        response += "Guess #" + str(guessCount) + ": " + str(guessNum) + "\n"
        if guessCount == 1:
            closeNew = abs(guessNum - secretNumber)
            if guessNum < secretNumber:
                response += "Your guess is too low! You have " + str(guessLeft) + " more " + str(turns) + ".\n"
            elif guessNum > secretNumber:
                response += 'Your guess is too high! You have ' + str(guessLeft) + " more " + str(turns) + ".\n"
            else:
                response += "No way, " + playerName + "! You guessed it on the first try! \n"
                break
        elif guessCount < guessNumber:
            closeOld = closeNew
            closeNew = abs(guessNum - secretNumber)
            warmer: bool = closeNew < closeOld
            colder = closeNew > closeOld
            if closeNew == 0:
                response += "You win " + playerName + f"! It took you {triesTaken} {turns}\n"
                break
            elif warmer:
                response += "You are getting warmer. You have " + str(guessLeft) + " more " + str(turns)
            elif colder:
                response += "You are getting colder. You have " + str(guessLeft) + " more " + str(turns)
        else:
            if guessNum == secretNumber:
                response += "You win " + playerName + "! It took you " + str(triesTaken) + " tries.\n"
                break
            else:
                response += 'Game over! The real number was ' + str(secretNumber) + '.\n'

        easygui.msgbox(response)


def main():
    playerName = easygui.enterbox("Welcome. What is your name?")

    guessNumber, maxNumber, secretNumber = initialize_game()

    play_game(playerName, guessNumber, maxNumber, secretNumber)


if __name__ == "__main__":
    main()

