import random

def guessing_game():
    '''An interactive guessing game where players guess a number 1-100 inclusive. Author: Chance Manning'''
    num = random.randint(1, 100)
    tries = 5

    print("I'm thinking of a number between 1 and 100")
    print("Guess what it is. You have", tries, "tries")

    while(True):
        guess = int(input())
        if (guess == num):
            print("You got it!")
            break

        if (guess > num):
            tries -=1
            if (tries == 0):
                print("Nope! You lost. The number was", num)
                break
            print("Nope! Too high. Try again (" + str(tries), "tries left)")

        if (guess < num):
            tries -=1
            if (tries == 0):
                print("Nope! You lost. The number was", num)
                break
            print("Nope! Too low. Try again (" + str(tries), "tries left)")

    print("Do you want to play again? (Y/N)")
    again = input()

    if (again.lower() == "y"):
        guessing_game()

if __name__ == "__main__":
    guessing_game()