import pygame 
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
#Window title
pygame.display.set_caption("2DRunner")
#Set game fps speed (frame rate)
clock = pygame.time.Clock()

#create surface variable with size
#test_surface = pygame.Surface((100,200))
#fill the surface with a color
#test_surface.fill("Red")
on_ground_y = 300
#load image as surface
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
#to create text you first have to create an imagine of the text and put it as a surface 
#test_font = pygame.font.Font(font type , font size)
test_font = pygame.font.Font("font/Pixeltype.ttf" , 50)
#test_surface = test_font.render(text , AA , color)
#should be True if you r not working with pixel art 
test_surface = test_font.render("My game" , False , "Black")


#import snake
#convert the pictures with .convert to let pygame work easier with it
#convert alpha ignores the black and white background in a picture u want to seperate
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_x_pos = 600
snail_rect = snail_surface.get_rect(midbottom = (snail_x_pos, on_ground_y))

#import player 
player_surf = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_x_pos = 80
player_rect = player_surf.get_rect(midbottom = (player_x_pos,on_ground_y))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #event will trigger if mouse is moved
        if event.type == pygame.MOUSEMOTION: #.MOUSEBUTTONDOWN: .MOUSEBUTTONUP:
            #print(event.pos)
            pass
    #blit block image transfer --> put one surfave on another surface
    #surfaces are chronology orderer so now ground can be over sky
    #use the rectangle for pos to controll more precise where the object is
    screen.blit( sky_surface , (0,0) )
    screen.blit( ground_surface , (0,300) )
    screen.blit( test_surface , (300,50) )
    screen.blit( snail_surface , snail_rect )
    screen.blit( player_surf , player_rect)
    snail_rect.x -= 4
    
    #print(player_rect.left)
     
    # if player_rect.colliderect(snail_rect):
    #     print("collision")

    #get mouse position and use it to interact with rectangles
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())

    #reset snail 
    if snail_rect.right < 0 : 
        snail_rect.left = 800
    
   
    pygame.display.update()
    #set fps ceiling 60 times per second so the while loop wont run faster than 60 times per second
    clock.tick(60)