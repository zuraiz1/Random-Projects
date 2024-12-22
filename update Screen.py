import os

def draw(X , Y):

    for y in range(25):
        update = ""
        for x in range(25):
            if x == X - 1 and y == Y - 1 :
                update = update + "\033[91mD\033[0m" + "  "
            else:
                update = update + "o  "
        print(update)


while True:
    os.system("cls")
    X = int(input("Enter the X coordinate:"))
    Y = int(input("Enter the Y coordinate:"))
    draw(X, Y)
    os.system("pause")