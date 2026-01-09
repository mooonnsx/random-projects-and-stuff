red = int(input(("Red: ")))
green = int(input(("Green: ")))
blue = int(input(("Blue: ")))
rgb = [red, green, blue]
hex = []
base16 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
for x in range(3):
    firstnum = int(rgb[x]/16)
    secondnum = rgb[x]-int(rgb[x]/16)*16
    firstnum = base16[firstnum]
    secondnum = base16[secondnum]
    hex.append(firstnum)
    hex.append(secondnum)
print(f"Hex: #{hex[0]}{hex[1]}{hex[2]}{hex[3]}{hex[4]}{hex[5]}")
