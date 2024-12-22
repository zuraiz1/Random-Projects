NOS = int(input("Enter Number of Stars: "))
x = NOS

for i in range(0,NOS):

    for y in range(0,x):
        print('*', end="")
    print(f"\n")
    x -= 1