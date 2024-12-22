import pygame

pygame.init()

clock = pygame.time.Clock()

# DISPLAY #
Window_W , Window_H = 512,512

win = pygame.display.set_mode((Window_W,Window_H))
pygame.display.set_caption("Qr Code Generator")

screen = pygame.surface.Surface((49,49))

#Qr Array
Q_Array = [[0 for _ in range(49)] for _ in range(49)]

Message = input("What do u want to encode : ")
Encoded = Message.encode("utf-8")
Encoded_Message = ""


def add_alignment_patterns(Q_Array):
    # Add alignment patterns (for simplicity, using a 7x7 pattern)
    alignment_pattern = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ]
    
    # Place alignment patterns in the corners
    for i in range(7):
        for j in range(7):
            Q_Array[i][j] = alignment_pattern[i][j]  # Top-left
            Q_Array[i][48-j-1] = alignment_pattern[i][j]  # Top-right
            Q_Array[48-i-1][j] = alignment_pattern[i][j]  # Bottom-left
            Q_Array[48-i-1][48-j-1] = alignment_pattern[i][j]  # Bottom-right

add_alignment_patterns(Q_Array)

for b in Encoded:
    temp = bin(b).removeprefix("0b")
    
    if len(temp) < 8:
        temp = "0"*(8-len(temp))+temp

    Encoded_Message += temp

# Filling data #
def filling_data(Array: list[list], Message: str):
    Count_x, Count_y = 48, 48  # Start from the bottom-right corner
    direction = -1  # Start filling upwards

    for bit in Message:
        # Check if the current position is reserved (alignment pattern)
        while Array[Count_y][Count_x] != 0:  # 0 means it's empty
            if direction == -1:  # If moving upwards
                Count_y -= 1
                if Count_y < 0:  # If we reach the top, switch direction
                    Count_y = 0
                    Count_x -= 1  # Move left
                    direction = 1  # Change direction to downwards
            else:  # If moving downwards
                Count_y += 1
                if Count_y >= 49:  # If we reach the bottom, switch direction
                    Count_y = 48
                    Count_x -= 1  # Move left
                    direction = -1  # Change direction to upwards

        # Place the bit in the QR code array
        Array[Count_y][Count_x] = int(bit)

        # Move to the next position
        if direction == -1:  # Moving upwards
            Count_y -= 1
            if Count_y < 0:  # If we reach the top, switch direction
                Count_y = 0
                Count_x -= 1  # Move left
                direction = 1  # Change direction to downwards
        else:  # Moving downwards
            Count_y += 1
            if Count_y >= 49:  # If we reach the bottom, switch direction
                Count_y = 48
                Count_x -= 1  # Move left
                direction = -1  # Change direction to upwards


filling_data(Q_Array, Encoded_Message)
        

Run = True

while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
            

    # Screen Updates #
    for y in range(49):
        for x in range(49):
            if Q_Array[y][x] == 1:
                screen.set_at((x,y), (0,0,0))
            else:
                screen.set_at((x,y), (255,255,255))

    # Refreshing #
    screen_Up = pygame.transform.scale(screen, (Window_W,Window_H))
    win.blit(screen_Up, (0,0))
    
    pygame.display.update()


    clock.tick(15)