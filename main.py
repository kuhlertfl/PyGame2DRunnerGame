import pygame 
from sys import exit
import time

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surface = pixel_font.render(f"Score: {current_time //1000}" , False , (64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit( score_surface , score_rect)
    return current_time
def display_end_score(score_end):
    score_surface = pixel_font.render(f"Score: {score_end //1000}" , False , (64,64,64))
    score_rect = score_surface.get_rect(center = (600,50))
    screen.blit( score_surface , score_rect)
pygame.init()
screen = pygame.display.set_mode((800,400))
#Window title
pygame.display.set_caption("2DRunner")
#Set game fps speed (frame rate)
clock = pygame.time.Clock()
game_active = False
start_time = 0
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
pixel_font = pygame.font.Font("font/Pixeltype.ttf" , 50)
#test_surface = test_font.render(text , AA , color)
#should be True if you r not working with pixel art 





#Setup Score
score = 0
score_message = pixel_font.render(f"Your Score: {score //1000}" , False , (64,64,64))
score_message_rect = score_message.get_rect(center = (650,50))

#import snake
#convert the pictures with .convert to let pygame work easier with it
#convert alpha ignores the black and white background in a picture u want to seperate
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_x_pos = 600
snail_rect = snail_surface.get_rect(midbottom = (snail_x_pos, on_ground_y))
snail_speed = 0 

#import player 
player_surf = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_x_pos = 80
player_rect = player_surf.get_rect(midbottom = (player_x_pos,on_ground_y))
player_gravity = 0
player_jumping_surf = pygame.image.load("graphics/player/jump.png").convert_alpha()
player_walking_surf = pygame.image.load("graphics/player/player_walk_2.png").convert_alpha()
player_walking = False



#Game Over Player --> make the player picture bigger 
player_standing = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
scale_factor_player = 3.2
new_size = (player_standing.get_width() * scale_factor_player , player_standing.get_height() * scale_factor_player)
scaled_player_surf = pygame.transform.scale(player_standing , new_size)
scaled_player_rect = scaled_player_surf.get_rect(center = (400,200))

#Game Over Text
player_standing = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
game_over_surface = pixel_font.render("PixelRunner" , False , (64,64,64))
game_over_rect = game_over_surface.get_rect(center = (400,50))
play_again_surface = pixel_font.render("Press Space to play again" , False , (64,64,64))
play_again_rect = play_again_surface.get_rect(center = (400,350))
#game state 
game_state = "game"

#Scroll sky and ground
# Initialize ground positions
ground_x_pos = 0
ground_x_pos_2 = ground_surface.get_width()  # Place the second ground immediately after the first

# Initialize sky positions
sky_x_pos = 0
sky_x_pos_2 = sky_surface.get_width()  # Place the second sky immediately after the first

#Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer , 900)


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #check if the game is active
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN: #.MOUSEBUTTONDOWN: .MOUSEBUTTONUP:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
                pass
            #Keyboard input in the event loop --> check if any button was pressed --> work with a specific key 
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom == 300:
                    
                        player_gravity = -20
        #if the game is not active
        else: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                
                snail_rect.left = 800
                game_active = True
                start_time = pygame.time.get_ticks()
        if event.type == obstacle_timer and game_active:
            print("Test")
    #blit block image transfer --> put one surfave on another surface
    #surfaces are chronology orderer so now ground can be over sky
    #use the rectangle for pos to controll more precise where the object is
    
    #Active Game

    if game_active:
        #====================Scroll sky and ground====================
        # Scroll ground
        # ground_x_pos -= 5  # Speed
        # ground_x_pos_2 -= 5
        # if ground_x_pos <= -ground_surface.get_width():
        #     ground_x_pos = ground_surface.get_width()
        # if ground_x_pos_2 <= -ground_surface.get_width():
        #     ground_x_pos_2 = ground_surface.get_width()
            
        # Scroll sky
        # sky_x_pos -= 2  # Slower speed
        # sky_x_pos_2 -= 2
        # if sky_x_pos <= -sky_surface.get_width():
        #     sky_x_pos = sky_surface.get_width()
        # if sky_x_pos_2 <= -sky_surface.get_width():
        #     sky_x_pos_2 = sky_surface.get_width()

        # Draw the sky and ground surfaces at their new positions
        screen.blit(sky_surface, (sky_x_pos, 0))
        screen.blit(sky_surface, (sky_x_pos_2, 0))
        screen.blit(ground_surface, (ground_x_pos, 300))
        screen.blit(ground_surface, (ground_x_pos_2, 300))

        #=============================================================
        #screen.blit( sky_surface , (0,0) )
        #screen.blit( ground_surface , (0,300) )
        #pygame.draw. --> the thing you want to draw (surface , color , rectangle you want to draw, width , border radius)
        
        
        score = display_score()
        screen.blit( snail_surface , snail_rect )

        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300 :
            player_rect.bottom = 300
        if player_rect.bottom >= 300:
            if (pygame.time.get_ticks()//100)  % 2 == 0:
                screen.blit( player_surf , player_rect)
            else:
                screen.blit( player_walking_surf , player_rect)
            
        if player_rect.bottom < 300:
            screen.blit( player_jumping_surf , player_rect)
        
        #Snail
        #snail_speed -= 0.01
        snail_rect.x -= 6 - snail_speed
        #reset snail 
        if snail_rect.right < 0 : 
            snail_rect.left = 800
        #print(player_rect.left)
        
        #collision player -- snail
        if player_rect.colliderect(snail_rect):
            print("Game Over")
            
            game_active = False
            
        #get mouse position and use it to interact with rectangles
        mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos):
        #     #print(pygame.mouse.get_pressed())
        #     pass
        
        
    else:
        screen.fill("#a0e0fc")
        screen.blit(scaled_player_surf , scaled_player_rect)
        screen.blit(game_over_surface , game_over_rect)
        screen.blit(play_again_surface , play_again_rect)
        score_message = pixel_font.render(f"Your Score: {score //1000}" , False , (64,64,64))
        score_message_rect = score_message.get_rect(center = (650,50))
        screen.blit(score_message , score_message_rect)
        

        


    pygame.display.update()
    #set fps ceiling 60 times per second so the while loop wont run faster than 60 times per second
    clock.tick(60)  
    