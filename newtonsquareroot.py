# Simple square root approximation using a hybrid Newton's method

num = float(input("Enter a Number: "))
iterations = int(input("How many iterations? "))
x=0
while (x*x < num): #initial guess, sets starting point
    x+=1
for a in range(iterations): 
    x = (x+num/x)/2
    if x*x == num: # stops if reaches exact sqrt
        break
print(f"the square root of {num} after {iterations} iterations is {x}")