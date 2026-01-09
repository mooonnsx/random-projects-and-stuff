hex = input("Hex Value: ").lower()
base16 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
if hex[0] == "#":
    hex = hex[1:len(hex)+2]
hexlist = []
for x in range(len(hex)):
    hexlist.append(hex[x])
for x in range(len(hexlist)):
    hexlist[x] = base16.index(hexlist[x])
print(f"Red: {hexlist[0]*16+hexlist[1]}\nGreen: {hexlist[2]*16+hexlist[3]}\nBlue: {hexlist[4]*16+hexlist[5]}")
