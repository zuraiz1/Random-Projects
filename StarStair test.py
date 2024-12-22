def INPUT(prompt):
    i = True
    while i == True:
        In = input(f"{prompt}")
        Digit = In.isdigit()
        if Digit == True:
            i = False
            return int(In)
            
        else:
            print("Invalid Input")
            i = True

Num = INPUT("Enter a Number: ")
line = ""

SCounter1 = 0
SPCounter1 = 1
SCounter2 = 0
SPCounter2 = Num - 1

for i in range(0,Num):
    for star in range(0, Num - SCounter1):
        line += ' '
    SCounter1 += 1

    for space in range(0, SPCounter1):
        line += '*'
    SPCounter1 += 1

    for star in range(0, SCounter2 + 1):
        line += '*'
    SCounter2 += 1
    
    for space in range(0, SPCounter2):
        line += ' '
    SPCounter2 -= 1

    print(line)
    line = ""

SCounter1 = 1
SPCounter1 = Num
SCounter2 = 0
SPCounter2 = 1

for i in range(0,Num):
    for star in range(0, SCounter1):
        line += ' '
    SCounter1 += 1

    for space in range(0, SPCounter1):
        line += '*'
    SPCounter1 -= 1

    for star in range(0, Num - SCounter2):
        line += '*'
    SCounter2 += 1

    for space in range(0, SPCounter2):
        line += ' '
    SPCounter2 += 1
    
    print(line)
    line = ""