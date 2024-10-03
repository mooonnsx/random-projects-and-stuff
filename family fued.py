print("Welcome to Family Feud!")
print("Category is: Boring Classes")
print("There are 3 answers up on the board.")
guess = input("What is: ")
english = False
government = False
math = False
strikes = 0
points = 0
while (english == False or government == False or math == False) and strikes < 3:
    if (guess == "English" or guess == "english" or guess == "Government" or guess == "government" or guess == "gov" or guess == "Gov" or guess == "history" or guess == "History" or guess == "social studies" or guess == "Social Studies" or guess == "Social studies" or guess == "social Studies" or guess == "Math" or guess == "math" or guess == "algebra" or guess == "Algebra" or guess == "algebra 1" or guess == "algebra 2" or guess == "Algebra 1" or guess == "Algebra 2" or guess == "geometry" or guess == "Geometry" or guess == "calculus" or guess == "Calculus" or guess == "Calc" or guess == "calc" or guess == "precalc" or guess == "pre-calc" or guess == "precalculus" or guess == "pre-calculus" or guess == "pre calc" or guess == "pre calculus" or guess == "Precalc" or guess == "Pre-calc" or guess == "Pre-Calc" or guess == "Precalculus" or guess == "Pre-Calculus" or guess == "Pre-calculus" or guess == "Pre calc" or guess == "Pre calculus" or guess == "mathematics" or guess == "Mathematics" or guess == "Maths" or guess == "maths"):
        if (guess == "English" or guess == "english"):
            if english == True:
                strikes += 1
                print("You already said that!") 
                print(f"You have {strikes} strikes. {3 - strikes} more and you lose!")
            else:   
                points += 33
                print("English is the number 2 answer.")
                print(f"That gives you 33 points. You now have {points} points.")
                english = True
                guess = "none"
            if (english == True and government == True and math == True):
                print("Well Done!")
                pass
            else: 
                guess = input("What is: ")
        if (guess == "Government" or guess == "government" or guess == "gov" or guess == "Gov" or guess == "history" or guess == "History" or guess == "social studies" or guess == "Social Studies" or guess == "Social studies" or guess == "social Studies"):
            if government == True:
                strikes += 1
                print("You already said that!") 
                print(f"You have {strikes} strikes. {3 - strikes} more and you lose!")
            else:   
                points += 28
                print("Government is the number 3 answer.")
                print(f"That gives you 28 points. You now have {points} points.")
                government = True
                guess = "none"
            if (english == True and government == True and math == True):
                print("You won! Well done!")
                pass
            else: 
                guess = input("What is: ")
        if (guess == "Math" or guess == "math" or guess == "algebra" or guess == "Algebra" or guess == "algebra 1" or guess == "algebra 2" or guess == "Algebra 1" or guess == "Algebra 2" or guess == "geometry" or guess == "Geometry" or guess == "calculus" or guess == "Calculus" or guess == "Calc" or guess == "calc" or guess == "precalc" or guess == "pre-calc" or guess == "precalculus" or guess == "pre-calculus" or guess == "pre calc" or guess == "pre calculus" or guess == "Precalc" or guess == "Pre-calc" or guess == "Pre-Calc" or guess == "Precalculus" or guess == "Pre-Calculus" or guess == "Pre-calculus" or guess == "Pre calc" or guess == "Pre calculus" or guess == "mathematics" or guess == "Mathematics" or guess == "Maths" or guess == "maths"):
            if math == True:
                strikes += 1
                print("You already said that!") 
                print(f"You have {strikes} strikes. {3 - strikes} more and you lose!")
            else:   
                points += 39
                print("Math is the number 1 answer!")
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