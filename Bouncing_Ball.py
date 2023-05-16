'''import pygame,sys
pygame.init()
screen=pygame.display.set_mode((500,300))
ball_rect = pygame.draw.circle(screen,color=(255,0,0),center=[50,50],radius=30)
pygame.display.set_caption("Bouncing Ball")
spd = [2,2]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0,0,0))
    ball_rect = ball_rect.move(spd)
    if ball_rect.left <= 0 or ball_rect >= 500:
        spd[0] = -spd[0]
    if ball_rect.top <= 0 or ball_rect.bottom >= 300:
        spd[1] = -spd[1]
    pygame.draw.circle(screen,col=(255,0,0),center=ball_rect,radius=30)
    pygame.display.flip()
'''


'''import pygame
pygame.init()
width,height = 1500,900
scrn = (width, height)
pygame.display.set_caption("Bouncing Ball")
screen = pygame.display.set_mode(scrn)
ball_obj = pygame.draw.circle(screen,((255,0,0)),([100,100]),radius = 30)
speed = [1,1]
while True:
    screen.fill((0,0,0))
    ball_obj = ball_obj.move(speed)
    if ball_obj.left <= 0 or ball_obj.right >= width:
        speed[0] = -speed[0]
    if ball_obj.top <= 0 or ball_obj.bottom >= height:
        speed[1] = -speed[1]
    pygame.draw.circle(screen,((255,0,0)),ball_obj.center,radius = 30)
    pygame.display.flip()'''


'''
import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

square_rect = pygame.Rect(100, 100, 100, 100)
rectangle_rect = pygame.Rect(300, 200, 200, 100)

# Set initial speeds
square_speed = [2, 0]
rectangle_speed = [-1, 1]

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))

    # Update positions
    square_rect = square_rect.move(square_speed)
    rectangle_rect = rectangle_rect.move(rectangle_speed)

    # Check for collisions with screen boundaries
    if square_rect.left <= 0 or square_rect.right >= width:
        square_speed[0] = -square_speed[0]
    if square_rect.top <= 0 or square_rect.bottom >= height:
        square_speed[1] = -square_speed[1]
    
    if rectangle_rect.left <= 0 or rectangle_rect.right >= width:
        rectangle_speed[0] = -rectangle_speed[0]
    if rectangle_rect.top <= 0 or rectangle_rect.bottom >= height:
        rectangle_speed[1] = -rectangle_speed[1]

    pygame.draw.rect(screen, (255, 0, 0), square_rect)
    pygame.draw.rect(screen, (0, 255, 0), rectangle_rect)

    pygame.display.flip()
    clock.tick(60)  # Limit the frame rate to 60 FPS
'''



import pygame
import random

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dinosaur Game")

# Load the dinosaur image
dino_image = pygame.image.load('dinosaur.png')
dino_width = 50
dino_height = 50
dino_image = pygame.transform.scale(dino_image, (dino_width, dino_height))

# Set up the player rectangle
player_x = 50
player_y = screen_height - dino_height - 10
player_rect = pygame.Rect(player_x, player_y, dino_width, dino_height)
jumping = False
jump_count = 20

# Set up the obstacle rectangle
obstacle_width = 50
obstacle_height = 50
obstacle_x = screen_width
obstacle_y = screen_height - obstacle_height - 10
obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
obstacle_speed = 5

# Set up the score
score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                jumping = True

    if jumping:
        if jump_count >= -20:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_rect.y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = 20

    screen.fill(WHITE)  # Set background color to white

    screen.blit(dino_image, player_rect)  # Draw the dinosaur image
    pygame.draw.rect(screen, BLACK, obstacle_rect)  # Set obstacle rectangle color to black

    obstacle_rect.x -= obstacle_speed

    if obstacle_rect.right <= 0:
        obstacle_rect.x = screen_width
        obstacle_rect.y = screen_height - obstacle_height - 10
        score += 1

    if player_rect.colliderect(obstacle_rect):
        game_over = True

    # Draw the score
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)  # Limit the frame rate to 60 FPS

pygame.quit()





