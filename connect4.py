#intro and instructions
win = False
lastinput = ""
c1 = ["□","□","□","□","□","□", 0]
c2 = ["□","□","□","□","□","□", 0]
c3 = ["□","□","□","□","□","□", 0]
c4 = ["□","□","□","□","□","□", 0]
c5 = ["□","□","□","□","□","□", 0]
c6 = ["□","□","□","□","□","□", 0]
c7 = ["□","□","□","□","□","□", 0]
xhas = []
ohas = []
def checkwinstates():
    global win
    # VERTICAL WIN STATE CHECK
    if lastinput == "p1input":
        if p1input == "1":
            if c1[c1[6]-2] == "X" and c1[c1[6]-3] == "X" and c1[c1[6]-4] == "X":
                print("Player 1 Wins!")
                win = True
        if p1input == "2":
            if c2[c2[6]-2] == "X" and c2[c2[6]-3] == "X" and c2[c2[6]-4] == "X":
                print("Player 1 Wins!")
                win = True
        if p1input == "3":
            if c3[c3[6]-2] == "X" and c3[c3[6]-3] == "X" and c3[c3[6]-4] == "X":
                print("Player 1 Wins!")
                win = True
        if p1input == "4":
            if c4[c4[6]-2] == "X" and c4[c4[6]-3] == "X" and c4[c4[6]-4] == "X":
                print("Player 1 Wins!")
                win = True
        if p1input == "5":
            if c5[c5[6]-2] == "X" and c5[c5[6]-3] == "X" and c5[c5[6]-4] == "X":
                print("Player 1 Wins!")
                win = True
        if p1input == "6":
            if c6[c6[6]-2] == "X" and c6[c6[6]-3] == "X" and c6[c6[6]-4] == "X":
                print("Player 1 Wins!")
                win = True
        if p1input == "1":
            if c7[c7[6]-2] == "X" and c7[c7[6]-3] == "X" and c7[c7[6]-4] == "X":
                print("Player 1 Wins!")
                win = True
    if "p2input" in globals() and lastinput == "p2input":
        if p2input == "1":
           if c1[c1[6]-2] == "O" and c1[c1[6]-3] == "O" and c1[c1[6]-4] == "O":
               print("Player 2 Wins!")
               win = True
        if p2input == "2":
           if c2[c2[6]-2] == "O" and c2[c2[6]-3] == "O" and c2[c2[6]-4] == "O":
               print("Player 2 Wins!")
               win = True
        if p2input == "3":
           if c3[c3[6]-2] == "O" and c3[c3[6]-3] == "O" and c3[c3[6]-4] == "O":
               print("Player 2 Wins!")
               win = True
        if p2input == "4":
           if c4[c4[6]-2] == "O" and c4[c4[6]-3] == "O" and c4[c4[6]-4] == "O":
               print("Player 2 Wins!")
               win = True
        if p2input == "5":
           if c5[c5[6]-2] == "O" and c5[c5[6]-3] == "O" and c5[c5[6]-4] == "O":
               print("Player 2 Wins!")
               win = True
        if p2input == "6":
           if c6[c6[6]-2] == "O" and c6[c6[6]-3] == "O" and c6[c6[6]-4] == "O":
               print("Player 2 Wins!")
               win = True
        if p2input == "1":
           if c7[c7[6]-2] == "O" and c7[c7[6]-3] == "O" and c7[c7[6]-4] == "O":
               print("Player 2 Wins!")
               win = True
    # HORIZONTAL WIN STATE CHECK
    if lastinput == "p1input":
        if p1input == "1":
            if c2[c1[6]-1] == "X" and c3[c1[6]-1] == "X" and c4[c1[6]-1] == "X":
                print("Player 1 Wins!")
                win = True
        if p1input == "2":
            if (c1[c2[6]-1] == "X" and c3[c2[6]-1] == "X" and c4[c2[6]-1] == "X") or (c3[c2[6]-1] == "X" and c4[c2[6]-1] == "X" and c5[c2[6]-1] == "X"):
                print("Player 1 Wins!")
                win = True
        if p1input == "3":
            if (c1[c3[6]-1] == "X" and c2[c3[6]-1] == "X" and c4[c3[6]-1] == "X") or (c2[c3[6]-1] == "X" and c4[c3[6]-1] == "X" and c5[c3[6]-1] == "X") or (c4[c3[6]-1] == "X" and c5[c3[6]-1] == "X" and c6[c3[6]-1] == "X"):
                print("Player 1 Wins!")
                win = True
        if p1input == "4":
            if (c1[c4[6]-1] == "X" and c2[c4[6]-1] == "X" and c3[c4[6]-1] == "X") or (c2[c4[6]-1] == "X" and c3[c4[6]-1] == "X" and c5[c4[6]-1] == "X") or (c3[c4[6]-1] == "X" and c5[c4[6]-1] == "X" and c6[c4[6]-1] == "X") or (c5[c4[6]-1] == "X" and c6[c4[6]-1] == "X" and c7[c4[6]-1] == "X"):
                print("Player 1 Wins!")
                win = True
        if p1input == "5":
            if (c2[c5[6]-1] == "X" and c3[c5[6]-1] == "X" and c4[c5[6]-1] == "X") or (c3[c5[6]-1] == "X" and c4[c5[6]-1] == "X" and c6[c5[6]-1] == "X") or (c4[c5[6]-1] == "X" and c6[c5[6]-1] == "X" and c7[c5[6]-1] == "X"):
                print("Player 1 Wins!")
                win = True
        if p1input == "6":
            if (c3[c6[6]-1] == "X" and c4[c6[6]-1] == "X" and c5[c6[6]-1] == "X") or (c4[c6[6]-1] == "X" and c5[c6[6]-1] == "X" and c7[c6[6]-1] == "X"):
                print("Player 1 Wins!")
                win = True
        if p1input == "7":
            if (c4[c7[6]-1] == "X" and c5[c7[6]-1] == "X" and c6[c7[6]-1] == "X"):
                print("Player 1 Wins!")
                win = True
    if "p2input" in globals() and lastinput == "p2input":
        if p2input == "1":
            if c2[c1[6]-1] == "O" and c3[c1[6]-1] == "O" and c4[c1[6]-1] == "O":
                print("Player 2 Wins!")
                win = True
        if p2input == "2":
            if (c1[c2[6]-1] == "O" and c3[c2[6]-1] == "O" and c4[c2[6]-1] == "O") or (c3[c2[6]-1] == "O" and c4[c2[6]-1] == "O" and c5[c2[6]-1] == "O"):
                print("Player 2 Wins!")
                win = True
        if p2input == "3":
            if (c1[c3[6]-1] == "O" and c2[c3[6]-1] == "O" and c4[c3[6]-1] == "O") or (c2[c3[6]-1] == "O" and c4[c3[6]-1] == "O" and c5[c3[6]-1] == "O") or (c4[c3[6]-1] == "O" and c5[c3[6]-1] == "O" and c6[c3[6]-1] == "O"):
                print("Player 2 Wins!")
                win = True
        if p2input == "4":
            if (c1[c4[6]-1] == "O" and c2[c4[6]-1] == "O" and c3[c4[6]-1] == "O") or (c2[c4[6]-1] == "O" and c3[c4[6]-1] == "O" and c5[c4[6]-1] == "O") or (c3[c4[6]-1] == "O" and c5[c4[6]-1] == "O" and c6[c4[6]-1] == "O") or (c5[c4[6]-1] == "O" and c6[c4[6]-1] == "O" and c7[c4[6]-1] == "O"):
                print("Player 2 Wins!")
                win = True
        if p2input == "5":
            if (c2[c5[6]-1] == "O" and c3[c5[6]-1] == "O" and c4[c5[6]-1] == "O") or (c3[c5[6]-1] == "O" and c4[c5[6]-1] == "O" and c6[c5[6]-1] == "O") or (c4[c5[6]-1] == "O" and c6[c5[6]-1] == "O" and c7[c5[6]-1] == "O"):
                print("Player 2 Wins!")
                win = True
        if p2input == "6":
            if (c3[c6[6]-1] == "O" and c4[c6[6]-1] == "O" and c5[c6[6]-1] == "O") or (c4[c6[6]-1] == "O" and c5[c6[6]-1] == "O" and c7[c6[6]-1] == "O"):
                print("Player 2 Wins!")
                win = True
        if p2input == "7":
            if (c4[c7[6]-1] == "O" and c5[c7[6]-1] == "O" and c6[c7[6]-1] == "O"):
                print("Player 2 Wins!")
                win = True
    #diagonal win state check
    if lastinput == "p1input":
        if (str(int(xhas[-1]) + 11) in xhas and str(int(xhas[-1]) - 11) in xhas and str(int(xhas[-1]) - 22) in xhas) or (str(int(xhas[-1]) - 33) in xhas and str(int(xhas[-1]) - 22) in xhas and str(int(xhas[-1]) - 11) in xhas) or (str(int(xhas[-1]) - 11) in xhas and str(int(xhas[-1]) + 11) in xhas and str(int(xhas[-1]) + 22) in xhas) or (str(int(xhas[-1]) + 11) in xhas and str(int(xhas[-1]) + 22) in xhas and str(int(xhas[-1]) + 33) in xhas): 
            print("Player 1 Wins!")
            win = True
        if (str(int(xhas[-1]) - 27) in xhas and str(int(xhas[-1]) - 18) in xhas and str(int(xhas[-1]) - 9) in xhas) or (str(int(xhas[-1]) - 18) in xhas and str(int(xhas[-1]) - 9) in xhas and str(int(xhas[-1]) + 9) in xhas) or (str(int(xhas[-1]) + -9) in xhas and str(int(xhas[-1]) + 9) in xhas and str(int(xhas[-1]) + 18) in xhas) or (str(int(xhas[-1]) + 9) in xhas and str(int(xhas[-1]) + 18) in xhas and str(int(xhas[-1]) + 27) in xhas):
            print("Player 1 Wins!")
            win = True
    elif lastinput == "p2input":
        if (str(int(ohas[-1]) + 11) in ohas and str(int(ohas[-1]) - 11) in ohas and str(int(ohas[-1]) - 22) in ohas) or (str(int(ohas[-1]) - 33) in ohas and str(int(ohas[-1]) - 22) in ohas and str(int(ohas[-1]) - 11) in ohas) or (str(int(ohas[-1]) - 11) in ohas and str(int(ohas[-1]) + 11) in ohas and str(int(ohas[-1]) + 22) in ohas) or (str(int(ohas[-1]) + 11) in ohas and str(int(ohas[-1]) + 22) in ohas and str(int(ohas[-1]) + 33) in ohas):
            print("Player 2 Wins!")
            win = True
        if (str(int(ohas[-1]) - 27) in ohas and str(int(ohas[-1]) - 18) in ohas and str(int(ohas[-1]) - 9) in ohas) or (str(int(ohas[-1]) - 18) in ohas and str(int(ohas[-1]) - 9) in ohas and str(int(ohas[-1]) + 9) in ohas) or (str(int(ohas[-1]) + -9) in ohas and str(int(ohas[-1]) + 9) in ohas and str(int(ohas[-1]) + 18) in ohas) or (str(int(ohas[-1]) + 9) in ohas and str(int(ohas[-1]) + 18) in ohas and str(int(ohas[-1]) + 27) in ohas):
            print("Player 2 Wins!")
            win = True

def printboard():
    print("-------------")
    print(c1[5],c2[5],c3[5],c4[5],c5[5],c6[5],c7[5])
    print(c1[4],c2[4],c3[4],c4[4],c5[4],c6[4],c7[4])
    print(c1[3],c2[3],c3[3],c4[3],c5[3],c6[3],c7[3])
    print(c1[2],c2[2],c3[2],c4[2],c5[2],c6[2],c7[2])
    print(c1[1],c2[1],c3[1],c4[1],c5[1],c6[1],c7[1])
    print(c1[0],c2[0],c3[0],c4[0],c5[0],c6[0],c7[0])
    print("1 2 3 4 5 6 7")
    print("-------------")
printboard()
while win != True:
    p1input = input("(X) Player 1: ")
    lastinput = "p1input"
    if p1input == "1":
        c1[c1[6]] = "X"
        c1[6] += 1
        xhas.append(f"1{c1[6]}")
    elif p1input == "2":
        c2[c2[6]] = "X"
        c2[6] += 1
        xhas.append(f"2{c2[6]}")
    elif p1input== "3":
        c3[c3[6]] = "X"
        c3[6] += 1
        xhas.append(f"3{c3[6]}")
    elif p1input == "4":
        c4[c4[6]] = "X"
        c4[6] += 1
        xhas.append(f"4{c4[6]}")
    elif p1input == "5":
        c5[c5[6]] = "X"
        c5[6] += 1
        xhas.append(f"5{c5[6]}")
    elif p1input == "6":
        c6[c6[6]] = "X"
        c6[6] += 1
        xhas.append(f"6{c6[6]}")
    elif p1input == "7":
        c7[c7[6]] = "X"
        c7[6] += 1
        xhas.append(f"7{c7[6]}")
    else:
        print("Your input was invalid.")
    printboard()
    checkwinstates()
    if win == True:
        break
    p2input = input("(O) Player 2: ")
    lastinput = "p2input"
    if p2input == "1":
        c1[c1[6]] = "O"
        c1[6] += 1
        ohas.append(f"1{c1[6]}")
    elif p2input == "2":
        c2[c2[6]] = "O"
        c2[6] += 1
        ohas.append(f"2{c2[6]}")
    elif p2input == "3":
        c3[c3[6]] = "O"
        c3[6] += 1
        ohas.append(f"3{c3[6]}")
    elif p2input == "4":
        c4[c4[6]] = "O"
        c4[6] += 1
        ohas.append(f"4{c4[6]}")
    elif p2input == "5":
        c5[c5[6]] = "O"
        c5[6] += 1
        ohas.append(f"5{c5[6]}")
    elif p2input == "6":
        c6[c6[6]] = "O"
        c6[6] += 1
        ohas.append(f"6{c6[6]}")
    elif p2input == "7":
        c7[c7[6]] = "O"
        c7[6] += 1
        ohas.append(f"7{c7[6]}")
    else:
        print("Your input was invalid.")
    printboard()
    checkwinstates()
    if win == True:
        break