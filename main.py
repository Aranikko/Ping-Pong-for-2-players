import pygame
import random

pygame.init()

screen = pygame.display.set_mode((640, 640))

fps = pygame.time.Clock()

running = True

player_1 = pygame.image.load('img/plt.png')
player_2 = pygame.image.load('img/plt.png')

player_1y = 300
player_2y = 300

ball = pygame.image.load('img/ball.png')
color_ball = (4, 209, 21)
ball_x = 300
ball_y = 300
ball_pos_1 = True
ball_pos_2 = False

a = 1
b = 0

col_1 = pygame.Surface((648, 20))
col_2 = pygame.Surface((648, 20))
col1_pos = False
col2_pos = False

col_3 = pygame.Surface((20, 648))
col_4 = pygame.Surface((20, 648))

Work = True
while running:
    if Work:

        key = pygame.key.get_pressed()

        screen.fill((255, 255, 255))


        def control_player_1():
            global player_1y
            if key[pygame.K_s] and player_1y < 590:
                player_1y += 5
            elif key[pygame.K_w] and player_1y > 0:
                player_1y -= 5


        screen.blit(player_1, (50, player_1y))
        player_1_rect = player_1.get_rect(topleft=(50, player_1y))

        control_player_1()


        def control_player_2():
            global player_2y
            if key[pygame.K_DOWN] and player_2y < 590:
                player_2y += 5
            elif key[pygame.K_UP] and player_2y > 0:
                player_2y -= 5


        control_player_2()
        screen.blit(player_2, (550, player_2y))
        player_2_rect = player_2.get_rect(topleft=(550, player_2y))

        screen.blit(ball, (ball_x, ball_y))
        ball_rect = ball.get_rect(topleft=(ball_x, ball_y))

        screen.blit(col_1, (0, 0))
        screen.blit(col_2, (0, 620))

        col_1_rect = col_1.get_rect(topleft=(0, 0))
        col_2_rect = col_2.get_rect(topleft=(0, 620))

        screen.blit(col_3, (0, 0))
        screen.blit(col_4, (620, 0))

        col_3_rect = col_3.get_rect(topleft=(0, 0))
        col_4_rect = col_4.get_rect(topleft=(620, 0))


        def b_cord():
            global b, a
            b = 0
            a = 0
            a = random.randint(1, 2)
            b = random.randint(1, 6)


        def b_cord_1():
            global b, a
            a = 0
            a = random.randint(1, 2)
            b = 0
            b = 1


        def moving_ball_1():
            global ball_x, ball_y
            ball_x += a
            ball_y += b


        def moving_ball_2():
            global ball_x, ball_y
            ball_x -= a
            ball_y -= b


        def col__2():
            global ball_x, ball_y
            ball_x -= a
            ball_y += b


        def col__1():
            global ball_x, ball_y
            ball_x += a
            ball_y -= b


        if col2_pos:
            col__2()
        elif col1_pos:
            col__1()

        if ball_pos_1:
            moving_ball_1()

        if ball_pos_2:
            moving_ball_2()

        if player_2_rect.colliderect(ball_rect):
            b_cord()
            ball_pos_2 = True
            ball_pos_1 = False
            col2_pos = False
            col1_pos = False

        if player_1_rect.colliderect(ball_rect):
            b_cord()
            ball_pos_2 = False
            ball_pos_1 = True
            col2_pos = False
            col1_pos = False

        if col_2_rect.colliderect(ball_rect):
            b_cord_1()
            col1_pos = True
            ball_pos_2 = False
            ball_pos_1 = False
            col2_pos = False

        if col_1_rect.colliderect(ball_rect):
            b_cord_1()
            col2_pos = True
            ball_pos_1 = False
            ball_pos_2 = False
            col1_pos = False

        if col_4_rect.colliderect(ball_rect) or col_3_rect.colliderect(ball_rect):
            Work = False
    else:
        key = pygame.key.get_pressed()
        if key[pygame.K_BACKSPACE]:
            Work = True
            ball_x = 300
            ball_y = 300
            player_1y = 300
            player_2y = 300
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    fps.tick(144)
