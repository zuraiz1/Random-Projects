# import 
import pygame, sys, random, time

pygame.init()

# Settings

Hight = 500
Length = 750
Fps = 60
clock = pygame.time.Clock()

# Score Display

font = pygame.font.SysFont('Bauhaus 93.ttf', 32, False, True)

# Music

# You Scored Screen

Score = font.render('You Scored', True, [230,230,230])
ScoreRect = Score.get_rect()

# Objects

Left_Score = 0
Right_Score = 0
player = pygame.Rect(0 , Hight/ 2 - 40,  7, 80)
opponent = pygame.Rect(740 , Hight/ 2 - 40,  7, 80)
ball = pygame.Rect(Length/2- 15, Hight/2 - 15, 15, 15)

Left_Side = pygame.Rect(0,0,Length/2, Hight)
Right_Side = pygame.Rect(Length/2, 0,Length, Hight)

# Ball Animation

ball_speed_x = 6
ball_speed_y = 6
player_speed = 0
opponent_speed = 0

## MAIN LOOP

running = True
    
while running == True:
        
    # Window
        
    screen = pygame.display.set_mode([Length, Hight])
    pygame.display.set_caption('Pong (AI)')
        
    # Event Handler
        
    ev = pygame.event.get()
        
    for event in ev:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
                
            if event.key == pygame.K_UP:
                opponent_speed = -8
                
            if event.key == pygame.K_DOWN:
                opponent_speed = 8
        
        if event.type == pygame.KEYUP:
                
            if event.key == pygame.K_UP:
                opponent_speed = 0
                
            if event.key == pygame.K_DOWN:
                opponent_speed = 0
        
    # Score
        #Left score

    Left = font.render(f'{Left_Score}', True, [230,230,230])
    LeftRect = Left.get_rect()
    LeftRect.center = [Length/2 - 25,30]

        #Right Score

    Right = font.render(f'{Right_Score}', True, [230,230,230])
    RightRect = Right.get_rect()
    RightRect.center = [Length/2 + 25,30]

    # Ball Movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # collision
    
    if ball.top <= 0 or ball.bottom >= 500:
        ball_speed_y *= -1
        
    if ball.left <= 0 or ball.right >= 750:
        
        if ball.left <= 0:
            Right_Score += 1
            
            ScoreRect.center = [Length - 187.5,Hight/ 2]
            
            
        else:
            Left_Score += 1
                        
            ScoreRect.center = [187.5,Hight/ 2]
            
        
        # Reposition
            # Players
        opponent.center = 743, Hight/2
        player.center = 6, Hight/2
        
            # ball
        ball.center = Length/2, Hight/2
        ball_speed_y *= random.choice((-1,1))
        ball_speed_x *= random.choice((-1,1))
        
        # Update
        # Fancy Background
        
        screen.fill([20,20,20])
        
        if ball.centerx > Length/2:
            pygame.draw.rect(screen, [25,25,25], Right_Side)
            pygame.draw.rect(screen, [50,50,50], Left_Side)
            
        elif ball.centerx < Length/2:
            pygame.draw.rect(screen, [25,25,25], Left_Side)
            pygame.draw.rect(screen, [50,50,50], Right_Side)
        
        else:
            screen.fill([25,25,25])
        
        # Everything Else
        pygame.draw.aaline(screen, [0,0,0], [Length/2, 0], [Length/2 , 500])
        pygame.draw.ellipse(screen, [255,255,255], ball)
        screen.blit(Left, LeftRect)
        screen.blit(Right, RightRect)
        screen.blit(Score, ScoreRect)
        pygame.draw.rect(screen, [150,150,150], player)
        pygame.draw.rect(screen, [150,150,150], opponent)
            
        pygame.display.flip()
        
        # Pause
        
        time.sleep(1.5)
    
    # Collision Detection
     
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
    
    # Player Movment
    
    player.y += player_speed
    
    if player.top >= ball.top:
        player_speed = -5.5
                
    if player.bottom <= ball.bottom:
        player_speed = 5.5
    
    if player.top <= 0:
        player.top = 0
    
    if player.bottom >= 500:
        player.bottom = 500
        
    # Opponent Movement
    
    opponent.y += opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    
    if opponent.bottom >= 500:
        opponent.bottom = 500
    
    # Update
        # Fancy Background
        
    screen.fill([20,20,20])
    
    if ball.centerx > Length/2:
        pygame.draw.rect(screen, [25,25,25], Right_Side)
        pygame.draw.rect(screen, [50,50,50], Left_Side)
        
    elif ball.centerx < Length/2:
        pygame.draw.rect(screen, [25,25,25], Left_Side)
        pygame.draw.rect(screen, [50,50,50], Right_Side)
    
    else:
        screen.fill([25,25,25])
        
    # Everything Else
    pygame.draw.aaline(screen, [0,0,0], [Length/2, 0], [Length/2 , 500],)
    pygame.draw.ellipse(screen, [255,255,255], ball)
    screen.blit(Left, LeftRect)
    screen.blit(Right, RightRect)
    pygame.draw.rect(screen, [150,150,150], player)
    pygame.draw.rect(screen, [150,150,150], opponent)
        
    pygame.display.flip()
    clock.tick(Fps)