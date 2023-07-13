import random
import easygui

def initialize_game():
    guessNumber = 10
    maxNumber = 20
    secretNumber = random.randint(1, maxNumber)

    return [guessNumber, maxNumber, secretNumber]


def play_game(playerName, guessNumber, maxNumber, secretNumber):
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

        if guessCount == 1:
            closeNew = abs(guessNum - secretNumber)
            if guessNum < secretNumber:
                easygui.msgbox("Your guess is too low! You have " + str(guessLeft) + " more turns, try again.")
            elif guessNum > secretNumber:
                easygui.msgbox('Your guess is too high! You have ' + str(guessLeft) + ' more turns, try again.')
            else:
                easygui.msgbox("No way, " + playerName + "! You guessed it on the first try! \n")
                break
        elif guessCount < guessNumber:
            closeOld = closeNew
            closeNew = abs(guessNum - secretNumber)
            warmer: bool = closeNew < closeOld
            colder = closeNew > closeOld
            if closeNew == 0:
                easygui.msgbox("You win " + playerName + f"! It took you {triesTaken} {turns}\n")
                break
            elif warmer:
                easygui.msgbox("You are getting warmer. You have " + str(guessLeft) + " more " + str(turns))
            elif colder:
                easygui.msgbox("You are getting colder. You have " + str(guessLeft) + " more " + str(turns))
        else:
            if guessNum == secretNumber:
                easygui.msgbox("You win " + playerName + "! It took you " + str(triesTaken) + " tries.\n")
                break
            else:
                easygui.msgbox('Game over! The real number was ' + str(secretNumber) + '.\n')


def main():
    playerName = easygui.enterbox("Welcome. What is your name?")

    guessNumber, maxNumber, secretNumber = initialize_game()

    play_game(playerName, guessNumber, maxNumber, secretNumber)


if __name__ == "__main__":
    main()
