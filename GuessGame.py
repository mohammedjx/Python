import random

userNum = True
print("Welcome to the Guessing game")
print("Please select a number from 0 to 10")
while userNum != "exit":
    randNum = random.randint(0, 10)
    userNum = int(input("Enter Number: "))
    if randNum - userNum == 0:
        print ("You guessed right")
        print("Random number is: ", randNum)
        break
    elif userNum == "exit":
        print("Thanks for playing")
        
    elif userNum != randNum:
        print("Try again\nRandom number was: ", randNum)
        randNum = 0
        
print ("¤¸¸.•´¯`•¸¸.•..>> ČŐŃĞŔĂŤÚĹĂŤĨŐŃŚ <<..•.¸¸•´¯`•.¸¸¤")