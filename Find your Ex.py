
import random,os

# NAND Gate
def nand(a,b):
    if a == True and b == True:
        return 0
    else:
        return 1


# Setting the Grid
grid = [[0 for colum in range(5)] for row in range(5)]

while True:
    #Player Position Starting
    PposX = 1
    PposY = 1
    movecounter = 0
    win = False

    # Spawning X # Makes sure its coordinates are not 1,1
    while True:
        XposX = random.randint(1,5)
        XposY = random.randint(1,5)

        if nand(XposX == 1 , XposY == 1):
            break

    # Main Game Loop
    while True:
        # Player INPUT

        os.system("cls")
        while True:
            for j in range(5):
                update= ""
                for i in range(5):
                    if PposY - 1 == j and PposX -1 == i :
                        update = update + "\033[91mP\033[0m" + "  "
                    else: 
                        update = update + "o  "
                print(update)

            print("8. UP\n2. Down\n4. Left\n6. Right\n")
            while True:
                move = input("move : ")
                if move != '':
                    move = int(move)
                    break
            if move == 8 or move == 2 or move == 4 or move == 6:
                break
            else:
                os.system("cls")
                print("Invalid Input")
                print("\n\n")

        print("\n\n")

        #Update player location

        if move == 8 and PposY-1 > 0 and movecounter <= 10:
            PposY -= 1
            movecounter += 1
        elif move == 2 and PposY+1 < 6 and movecounter <= 10:
            PposY += 1
            movecounter += 1
        elif move == 6 and PposX+1 < 6 and movecounter <= 10:
            PposX += 1
            movecounter += 1
        elif move == 4 and PposX-1 > 0 and movecounter <= 10:
            PposX -= 1
            movecounter += 1


        # Check for win
        if PposX == XposX and PposY == XposY and movecounter <= 10:
            win = True
            break
        elif movecounter == 10:
            win = False
            break

    if win == True:
        print("You Win")
    else:
        print("You Lose")

    os.system("pause")

    play = input("Do you want to play again (Y or N) : ")
    if play == "N" or play == "n" :
        break
    else:
        os.system("cls")