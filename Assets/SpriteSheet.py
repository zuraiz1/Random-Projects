import pygame

class Spritesheet():
    def __init__(self, sheet) -> None:
        self.sheet = sheet  ## This is the Sprite Sheet

    def extract(self, frame, width, hight, scale, Background_Color):
        image = pygame.Surface((width, hight)).convert_alpha()
        image.blit(self.sheet, (0,0), (frame * width), 0, width, hight)
        image = pygame.transform.scale(image, width * scale , hight * scale)


        return image
    
# example : Sprite_sheet = SpriteSheet.Spritesheet(pygame.image.load(<Destination>))
#           Sprite_sheet.extract(0, 32, 32, 2, [0 , 0 , 0])


## frame            : The index of image u want ( Starts with 0 )
## width            : Width of the image you want
## hight            : Height of the image you want
## scale            : the the scale factor for the image ( 1 for no scale up )
## Background_Color : The color of the background of the image to remove ( all transparent images gain black bg )