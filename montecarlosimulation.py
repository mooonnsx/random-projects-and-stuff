import random
def squareroot(num): # calculate square root using newton's square root method (original in separate python file)
    x=0
    while (x*x < num):
        x+=1
    for a in range(100): # 100 iterations
        x = (x+num/x)/2
        if x*x == num:
            break
    return (x)
yes = 0
no =0
iterations = int(input("How many iterations? "))
for a in range(iterations):
    x = random.random()
    y = random.random()
    if squareroot((x-.5)*(x-.5)+(y-.5)*(y-.5)) <= .5: # possible without using square root but fun concept
        yes += 1
    else:
        no +=1
print(f"your calculated pi value is {yes*4/(yes+no)}") # multiplied by 4 because otherwise output is pi/4