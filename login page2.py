user_data = {
    "user1": "bravo123",
    "user2": "alpha456",
    "user3": "charlie789"
}

usernameinput = input("Username: ")
if usernameinput in user_data:
    passwordinput = input("Password: ")
    if (user_data[usernameinput] != passwordinput):
        print("Incorrect password.")
    if (user_data[usernameinput] == passwordinput):
        print("Correct password.")
else:
    print("Username not found.")