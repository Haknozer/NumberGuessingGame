import random
import time
import json
import os
def main():
    rndNumber =  random.randint(1,100)
    chances = 0
    select = ""
    chancesCounter = 0
    correct = False
    record = []
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 chances to guess the correct number.")

    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    while True:
        
        if not os.path.exists("record.json"):
            open("record.json","x")
        try:
            with open ("record.json","r") as json_file:
                record = json.load(json_file)
                
        except:
                record = []
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
        start = time.time()
        chancesCounter += 1
        try:
            userGuess = int(input("Enter your guess: "))
        except ValueError:
            print("Only Number")
            chancesCounter -= 1

        if userGuess > rndNumber:
            print(f"Incorrect! The number is less than {userGuess}.")
        elif userGuess < rndNumber:
            print(f"Incorrect! The number is greater than {userGuess}.")
        else:
            end = time.time()
            length  = end - start
            print(f"Congratulations! You guessed the correct number in {chancesCounter} attempts. You found the correct number in {length} seconds")
            updateRecord(length,select,record)
            correct = True
            break

    if correct == False:
        print(f"The correct number was {rndNumber}")

    restart = input("Do you want to play again? Y/N : ")
    
    if restart.upper() == "Y":
        print("das")
        main()

def updateRecord(time,select,record):
    if select in record:
        for x in record:
            if x == select and record[x] > time:
                record[x] = time
    else:
        record[select] = time

    with open("record.json","w") as json_file:
        json.dump(record,json_file,indent=1)
main()