print("num1: ")
num1 = float(input())
num1original = num1
print("num2: ")
num2 = float(input())
num2original = num2
num3 = 0
print("iterations: ")
num4 = input()
print("------")
print(num1)
print(num2)
for x in range(0,int(num4)):
    num3 = num2
    num2+=num1
    num1 = num3
    print(num2)
print(f"golden ratio for the fibonacci sequence beginning with {num1original} and {num2original} as approximated after {num4} iterations:")
print(num2/num1)