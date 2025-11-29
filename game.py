import pygame
import sys

class TennisGame:

    def __init__(self, width=800, height=700):
        pygame.init()
        pygame.display.set_caption("Tennis")

        self.SCORE_NAMES = ["0", "15", "30", "40"]

        #Setup
        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()

        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((width, height))

        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)

        self.player_width = 50
        self.player_height = 10
        self.ball_size = 30

        self.FPS = 60

        #Players
        self.player1 = pygame.Rect(self.WIDTH - self.player_width * 2,
                                   self.HEIGHT - 50,
                                   self.player_width, self.player_height)

        self.player2 = pygame.Rect(self.player_width, 40,
                                   self.player_width, self.player_height)

        self.ball = pygame.Rect(self.WIDTH - 40, self.HEIGHT - 40,
                                self.ball_size, self.ball_size)

        # Ball
        self.ball_speed_x = 0
        self.ball_speed_y = 0

        # Scores
        self.score_p1 = 0
        self.score_p2 = 0

        self.waiting_for_serve = True
        self.game_over = False
        self.winner = None

    def start(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.waiting_for_serve:
                        self.waiting_for_serve = False
                        self.ball_speed_x = -5   
                        self.ball_speed_y = -5
            
            keys = pygame.key.get_pressed()
            move_p1 = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
            move_p2 = keys[pygame.K_d] - keys[pygame.K_q]

            self.update(move_p1, move_p2)

            self.screen.fill(self.BLACK)
            score_text = self.font.render(self.score_label(), True, self.WHITE)
            self.screen.blit(score_text, (self.WIDTH // 2 - 40, 10))


            if self.waiting_for_serve and not self.game_over:
                hint = self.font.render("Press SPACE to serve", True, self.WHITE)
                self.screen.blit(hint, (self.WIDTH//2 - 120, self.HEIGHT//2))

            pygame.draw.rect(self.screen, self.WHITE, self.player1)
            pygame.draw.rect(self.screen, self.WHITE, self.player2)
            pygame.draw.ellipse(self.screen, self.WHITE, self.ball)
            pygame.display.flip()
            self.clock.tick(self.FPS)

        winner = "Player 1" if self.score_p1 >= 5 else "Player 2"
        winner_display = self.font.render(f"{winner} wins", True, self.WHITE)
        self.screen.blit(winner_display, (self.WIDTH // 2 - 100 , self.HEIGHT // 2 ))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

    def update(self, move_p1, move_p2):
        if self.waiting_for_serve:
            self.ball.centerx = self.player1.centerx
            self.ball.bottom = self.player1.top
        else:
            if move_p1 < 0 and self.player1.left > 0:
                self.player1.x -= 10
            if move_p1 > 0 and self.player1.right < self.WIDTH:
                self.player1.x += 10

            if move_p2 < 0 and self.player2.left > 0:
                self.player2.x -= 10
            if move_p2 > 0 and self.player2.right < self.WIDTH:
                self.player2.x += 10

            self.ball.x += self.ball_speed_x
            self.ball.y += self.ball_speed_y
        
        self.check_colissions()


    def score(self, player):
        if player == 1:
            # Player 2 loses advantage, back to deuce
            if self.score_p2 >= 4 and (self.score_p2 - self.score_p1) == 1:
                self.score_p1 = 4
                self.score_p2 = 4
                self.waiting_for_serve = True
                return

            self.score_p1 += 1

            # win condition
            if self.score_p1 >= 4 and (self.score_p1 - self.score_p2) >= 2:
                self.game_over = True
                self.winner = 1

            self.waiting_for_serve = True
            return

        if player == 2:
            # Player 1 loses advantage, back to deuce
            if self.score_p1 >= 4 and (self.score_p1 - self.score_p2) == 1:
                self.score_p1 = 4
                self.score_p2 = 4
                self.waiting_for_serve = True
                return

            self.score_p2 += 1

            # win condition
            if self.score_p2 >= 4 and (self.score_p2 - self.score_p1) >= 2:
                self.game_over = True
                self.winner = 2

            self.waiting_for_serve = True
            return

    def reset_positions(self):
        self.waiting_for_serve = True
        self.ball_speed_x = 0
        self.ball_speed_y = 0
        self.player1.x = self.WIDTH  - self.player_width * 2
        self.player2.x = self.player_width

    def check_colissions(self):
        if self.ball.left <= 0 or self.ball.right >= self.WIDTH:
            self.ball_speed_x = -self.ball_speed_x

        if self.ball.colliderect(self.player1) and self.ball_speed_y > 0:
            self.ball_speed_y = -self.ball_speed_y
        if self.ball.colliderect(self.player2) and self.ball_speed_y < 0:
            self.ball_speed_y = -self.ball_speed_y
    
        if self.ball.top <= 0:
            self.score(1)
            self.reset_positions()
            
        if self.ball.bottom >= self.HEIGHT:
            self.score(2)
            self.reset_positions()
            
    def score_label(self):
        #TODO: return the score in tennis format (e.g., "15-30", "Deuce", "Advantage Player 1")
        return f"{self.score_p1}-{self.score_p2}"
    
if __name__ == "__main__":
    game = TennisGame()
    game.start()
