password = str("bravo123")
userInput = input("Password: ")
userInput = str(userInput)
while (password != userInput):
    print("Incorrect. Try Again.")
    userInput = input("Password: ")
print("Correct.")