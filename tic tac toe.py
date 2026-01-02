# old code, not optimized but fun to play around with. lacks documentation

board = {
    "spot1": "_",
    "spot2": "_",
    "spot3": "_",
    "spot4": "_",
    "spot5": "_",
    "spot6": "_",
    "spot7": "_",
    "spot8": "_",
    "spot9": "_"
}

print("Welcome to Tic Tac Toe")

while 1 == 1:
    print(f"---------\n| {board['spot1']} {board['spot2']} {board['spot3']} |\n| {board['spot4']} {board['spot5']} {board['spot6']} |\n| {board['spot7']} {board['spot8']} {board['spot9']} |\n---------")
    placex = input("Place X: ")
    if placex.isdigit() and int(placex) >= 1 and int(placex) <= 9:
        placex = int(placex) 
    else:
        print("You must enter a number between 1 and 9. Your turn is forfeitted.")
        placex = 0

    if placex == 1:
        if board['spot1'] == "_":
            board['spot1'] = "X"
        else: 
            print("That is taken! Your turn is forfeitted.")
    if placex == 2:
        if board['spot2'] == "_":
            board['spot2'] = "X"
        else: 
            print("That is taken! Your turn is forfeitted.")
    if placex == 3:
        if board['spot3'] == "_":
            board['spot3'] = "X"
        else: 
            print("That is taken! Your turn is forfeitted.")
    if placex == 4:
        if board['spot4'] == "_":
            board['spot4'] = "X"
        else: 
            print("That is taken! Your turn is forfeitted.")
    if placex == 5:
        if board['spot5'] == "_":
            board['spot5'] = "X"
        else: 
            print("That is taken! Your turn is forfeitted.")
    if placex == 6:
        if board['spot6'] == "_":
            board['spot6'] = "X"
        else: 
            print("That is taken! Your turn is forfeitted.")
    if placex == 7:
        if board['spot7'] == "_":
            board['spot7'] = "X"
        else: 
            print("That is taken! Your turn is forfeitted.")
    if placex == 8:
        if board['spot8'] == "_":
            board['spot8'] = "X"
        else: 
            print("That is taken! Your turn is forfeitted.")
    if placex == 9:
        if board['spot9'] == "_":
            board['spot9'] = "X"
        else: 
            print("That is taken! Your turn is forfeitted.")

    print(f"---------\n| {board['spot1']} {board['spot2']} {board['spot3']} |\n| {board['spot4']} {board['spot5']} {board['spot6']} |\n| {board['spot7']} {board['spot8']} {board['spot9']} |\n---------")

    if (board['spot1'] == "X" and board['spot2'] == "X" and board['spot3'] == "X") or (board['spot4'] == "X" and board['spot5'] == "X" and board['spot6'] == "X") or (board['spot7'] == "X" and board['spot8'] == "X" and board['spot9'] == "X") or (board['spot1'] == "X" and board['spot4'] == "X" and board['spot7'] == "X") or (board['spot2'] == "X" and board['spot5'] == "X" and board['spot8'] == "X") or (board['spot3'] == "X" and board['spot6'] == "X" and board['spot9'] == "X") or (board['spot1'] == "X" and board['spot5'] == "X" and board['spot9'] == "X") or (board['spot3'] == "X" and board['spot5'] == "X" and board['spot7'] == "X"):
        print("X wins!")
        break

    if board["spot1"] != "_" and board["spot2"] != "_" and board["spot3"] != "_" and board["spot4"] != "_" and board["spot5"] != "_" and board["spot6"] != "_" and board["spot7"] != "_" and board["spot8"] != "_" and board["spot9"] != "_":
        print("Tie Game!")
        break

    placeo = input("Place O: ")
    if placeo.isdigit() and int(placeo) >= 1 and int(placeo) <= 9:
        placeo = int(placeo)
    else:
        print("You must enter a number between 1 and 9. Your turn is forfeitted.")
        placeo = 0

    if placeo == 1:
        if board['spot1'] == "_":
            board['spot1'] = "O"
        else: 
            print("That is taken! Your turn is forfeitted.")
    if placeo == 2:
        if board['spot2'] == "_":
            board['spot2'] = "O"
        else: 
            print("That is taken! Your turn is forfeitted.")
    if placeo == 3:
        if board['spot3'] == "_":
            board['spot3'] = "O"
        else: 
            print("That is taken! Your turn is forfeitted.")
    if placeo == 4:
        if board['spot4'] == "_":
            board['spot4'] = "O"
        else: 
            print("That is taken! Your turn is forfeitted.")
    if placeo == 5:
        if board['spot5'] == "_":
            board['spot5'] = "O"
        else: 
            print("That is taken! Your turn is forfeitted.")
    if placeo == 6:
        if board['spot6'] == "_":
            board['spot6'] = "O"
        else: 
            print("That is taken! Your turn is forfeitted.")
    if placeo == 7:
        if board['spot7'] == "_":
            board['spot7'] = "O"
        else: 
            print("That is taken! Your turn is forfeitted.")
    if placeo == 8:
        if board['spot8'] == "_":
            board['spot8'] = "O"
        else: 
            print("That is taken! Your turn is forfeitted.")
    if placeo == 9:
        if board['spot9'] == "_":
            board['spot9'] = "O"
        else: 
            print("That is taken! Your turn is forfeitted.")

    if (board['spot1'] == "O" and board['spot2'] == "O" and board['spot3'] == "O") or (board['spot4'] == "O" and board['spot5'] == "O" and board['spot6'] == "O") or (board['spot7'] == "O" and board['spot8'] == "O" and board['spot9'] == "O") or (board['spot1'] == "O" and board['spot4'] == "O" and board['spot7'] == "O") or (board['spot2'] == "O" and board['spot5'] == "O" and board['spot8'] == "O") or (board['spot3'] == "O" and board['spot6'] == "O" and board['spot9'] == "O") or (board['spot1'] == "O" and board['spot5'] == "O" and board['spot9'] == "O") or (board['spot3'] == "O" and board['spot5'] == "O" and board['spot7'] == "O"):
        print(f"---------\n| {board['spot1']} {board['spot2']} {board['spot3']} |\n| {board['spot4']} {board['spot5']} {board['spot6']} |\n| {board['spot7']} {board['spot8']} {board['spot9']} |\n---------")
        print("O wins!")
        break

    if board["spot1"] != "_" and board["spot2"] != "_" and board["spot3"] != "_" and board["spot4"] != "_" and board["spot5"] != "_" and board["spot6"] != "_" and board["spot7"] != "_" and board["spot8"] != "_" and board["spot9"] != "_":
        print("Tie Game!")
        break