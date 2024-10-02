print("Welcome to Family Feud!")
print("Category is: Boring Classes")
guess = input("What is: ")
english = False
government = False
math = False
strikes = 0
points = 0
while (english == False or government == False or math == False) and strikes < 3:
    if (guess == "English" or guess == "Government" or guess == "Math"):
        if (guess == "English"):
            points += 33
            print(f"That gives you 33 points. You now have {points} points.")
            english = True
            guess = "none"
            if (english == True and government == True and math == True):
                print("Well Done!")
                pass
            else: 
                guess = input("What is: ")
        if (guess == "Government"):
            points += 28
            print(f"That gives you 28 points. You now have {points} points.")
            government = True
            guess = "none"
            if (english == True and government == True and math == True):
                print("You won! Well done!")
                pass
            else: 
                guess = input("What is: ")
        if (guess == "Math"):
            points += 39
            print(f"That gives you 39 points. You now have {points} points.")
            math = True
            guess = "none"
            if (english == True and government == True and math == True):
                print("Well done, you won!")
                pass
            else: 
                guess = input("What is: ")
    else:
        print("That is incorrect.")
        strikes += 1
        if (strikes == 3):
            print("You lost!")
            print(f"You finished with {points} points.")
        else: 
            print(f"You have {strikes} strikes. {3 - strikes} more and you lose!")
            guess = input("What is: ")