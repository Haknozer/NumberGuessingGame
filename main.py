import random

def main():
    rndNumber =  random.randint(1,100)
    chances = 0
    select = ""
    chancesCounter = 0
    correct = False
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 chances to guess the correct number.")

    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    while True:
        try:
            difficulty=int((input("Your choice : ")))

            if difficulty < 1 or difficulty > 3:
                raise ValueError("Do not enter numbers than less 1 or greater than 3")
            break
        except ValueError as e:
            if str(e) == "Do not enter numbers than less 1 or greater than 3":
                print(e)
            else:
                print("Only number")


    if difficulty == 1:
        select = "Easy"
        chances = 10
    elif difficulty == 2:
        select == "Medium"
        chances = 5
    else:
        select = "Hard" 
        chances = 3

    print(f"Great! You have selected the {select} difficulty level.")
    print("Let's start the game!")

    while chancesCounter != chances:
        chancesCounter += 1
        try:
            userGuess = int(input("Enter your guess: "))
        except ValueError:
            print("Only Number")

        if userGuess > rndNumber:
            print(f"Incorrect! The number is less than {userGuess}.")
        elif userGuess < rndNumber:
            print(f"Incorrect! The number is greater than {userGuess}.")
        else:
            print(f"Congratulations! You guessed the correct number in {chancesCounter} attempts.")
            correct = True
            break

    if correct == False:
        print(f"The correct number was {rndNumber}")

    restart = input("Do you want to play again? Y/N : ")
    
    if restart.upper() == "Y":
        print("das")
        main()
main()