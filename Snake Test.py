import os
import keyboard

snake = [[0 for colum in range(2)] for row in range(0)]

# Making the innitial 2 long snake
snake.append([0 , 0])
snake.append([1 , 0])
snake.append([2 , 0])
snake.append([3 , 0])
snake.append([4 , 0])

def draw(array):
    os.system("cls")

    for y in range(10):

        update = ""
        for x in range(10):

            XFound = False
            YFound = False

            for i in range(len(snake)):
                if array[i][0] == x and array[i][1] == y:
                    XFound = True
                    YFound = True

            if XFound == True and YFound == True:
                update += "\033[91mD\033[0m  "
            else:
                update += "o  "
        print(update)

def update(array, dir):

    for i in range(len(array) - 1):
        array[i][0] = array[i + 1][0]
        array[i][1] = array[i + 1][1]

    if dir == "Right":
        array[len(array)-1][0] += 1

    elif dir == "Left":
        array[len(array)-1][0] -= 1

    elif dir == "Up":
        array[len(array)-1][1] -= 1

    elif dir == "Down":
        array[len(array)-1][1] += 1

def check():
    global cangoUp, cangoDown, cangoLeft, cangoRight
    cangoUp = False
    cangoDown = False
    cangoLeft = False
    cangoRight = False

    #checks if we can move the snake in a direction

    ###### TO FIX.
    #the down works fine, but up, right, left and down dont work when the snake is in a straight line   

    for i in range(len(snake)):
        if snake[len(snake) -1][0] + 1 != snake[i][0] and snake[len(snake) -1][1] != snake[i][1]:
            cangoRight = True
        
        if snake[len(snake) -1][0] - 1 != snake[i][0] and snake[len(snake) -1][1] != snake[i][1]:
            cangoLeft = True
        
        if snake[len(snake) -1][0] != snake[i][0] and snake[len(snake) -1][1] - 1 != snake[i][1]:
            cangoUp = True
        
        if snake[len(snake) -1][0] + 1 != snake[i][0] and snake[len(snake) -1][1] + 1 != snake[i][1]:
            cangoDown = True
        
    # check for key presses
    if keyboard.is_pressed('up'):
        if cangoUp:
            update(snake , "Up")

    elif keyboard.is_pressed('down'):
        if cangoDown:
            update(snake , "Down")

    elif keyboard.is_pressed('left'):
        if cangoLeft:
            update(snake , "Left")

    elif keyboard.is_pressed('right'):
        if cangoRight:
            update(snake , "Right")


while True:

    check()
    draw(snake)
    print(cangoUp, cangoDown, cangoLeft, cangoRight)
   
    os.system("pause")