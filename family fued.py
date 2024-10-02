print("Category is: Boring Classes")
guess = input("What is: ")
english = False
government = False
math = False
strikes = 0
while (english == False or government == False or math == False and strikes < 3):
    if (guess == "English" or "Government" or "Math"):
        if (guess == "English"):
            print("23 points")
            english = True
            guess = "none"
            if (english == True and government == True and math == True):
                print("Well Done!")
                pass
            else: 
                guess = input("What is: ")
        if (guess == "Government"):
            print("20 points")
            government = True
            guess = "none"
            if (english == True and government == True and math == True):
                print("Well Done!")
                pass
            else: 
                guess = input("What is: ")
        if (guess == "Math"):
            print("31 points")
            math = True
            guess = "none"
            if (english == True and government == True and math == True):
                print("Well Done!")
                pass
            else: 
                guess = input("What is: ")
    else:
        print("Incorrect")
        strikes += 1
        if (strikes == 3):
            print("You lost!")
        else: 
            print(f"You have {strikes} strikes. {3 - strikes} more and you lose!")
            guess = input("What is: ")