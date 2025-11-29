# import pygame
# import sys
# import random

# pygame.init()
# font = pygame.font.Font(None, 36)
# clock = pygame.time.Clock()

# WIDTH, HEIGHT = 800,700
# FPS = 60

# WHITE = (255,255,255)
# BLACK = (0,0,0)

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Tennis")

# player_width, player_height = 50, 10
# player1 = pygame.Rect(WIDTH  - player_width * 2 , HEIGHT - 50, player_width, player_height)
# player2 = pygame.Rect(player_width, 40, player_width, player_height)

# ball = pygame.Rect(WIDTH - 30 - 10, HEIGHT - 30 - 10, 30, 30)
# ball_speed_x = 0             
# ball_speed_y = 0

# score_player_1 = 0
# score_player_2 = 0

# game_over = False
# waiting_for_serve = True  

# while not game_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE and waiting_for_serve:
#                 waiting_for_serve = False
#                 ball_speed_x = -5   
#                 ball_speed_y = -5
    
#     keys = pygame.key.get_pressed()

#     if waiting_for_serve:
#         ball.centerx = player1.centerx
#         ball.bottom = player1.top
#     else:
#         if keys[pygame.K_LEFT] and player1.left > 0:
#             player1.x -= 10
#         if keys[pygame.K_RIGHT] and player1.right < WIDTH:
#             player1.x += 10

#         if keys[pygame.K_q] and player2.left > 0:
#             player2.x -= 10
#         if keys[pygame.K_d] and player2.right < WIDTH:
#             player2.x += 10

#         ball.x += ball_speed_x
#         ball.y += ball_speed_y

#     if ball.left <= 0 or ball.right >= WIDTH:
#         ball_speed_x = -ball_speed_x

#     if ball.colliderect(player1) and ball_speed_y > 0:
#         ball_speed_y = -ball_speed_y
#     if ball.colliderect(player2) and ball_speed_y < 0:
#         ball_speed_y = -ball_speed_y
 
#     if ball.top <= 0:
#         score_player_1 += 1
#         waiting_for_serve = True
#         ball_speed_x = 0
#         ball_speed_y = 0
#         player1.x = WIDTH  - player_width * 2
#         player2.x = player_width

#     if ball.bottom >= HEIGHT:
#         score_player_2 += 1
#         waiting_for_serve = True
#         ball_speed_x = 0
#         ball_speed_y = 0
#         player1.x = WIDTH  - player_width * 2
#         player2.x = player_width

#     if score_player_1 >= 5 or score_player_2 >= 5:
#         game_over = True
#         waiting_for_serve = False

#     screen.fill(BLACK)
#     score_display = font.render(f"{score_player_1} - {score_player_2}", True, WHITE)
#     screen.blit(score_display, (WIDTH // 2 - 40, 10))

#     if waiting_for_serve and not game_over:
#         hint = font.render("Press SPACE to serve", True, WHITE)
#         screen.blit(hint, (WIDTH//2 - 120, HEIGHT//2))

#     pygame.draw.rect(screen, WHITE, player1)
#     pygame.draw.rect(screen, WHITE, player2)
#     pygame.draw.ellipse(screen, WHITE, ball)
#     pygame.display.flip()
#     clock.tick(FPS)
    
# winner = "Player 1" if score_player_1 >= 5 else "Player 2"
# winner_display = font.render(f"{winner} wins", True, WHITE)
# screen.blit(winner_display, (WIDTH // 2 - 100 , HEIGHT // 2 ))
# pygame.display.update()

# pygame.time.wait(3000)
# pygame.quit()
# sys.exit()
