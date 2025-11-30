import pygame
import sys

# Constants to avoid magic numbers
DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 700
PLAYER_SPEED = 10
INITIAL_BALL_SPEED_X = -5
INITIAL_BALL_SPEED_Y = -5
FONT_SIZE = 36
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 10
BALL_SIZE = 30
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCORE_NAMES = ["0", "15", "30", "40"]

class TennisGame:

    def __init__(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
        pygame.init()
  
        pygame.display.set_caption("Tennis")

        # Setup
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.clock = pygame.time.Clock()

        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((width, height))

        self.player_width = PLAYER_WIDTH
        self.player_height = PLAYER_HEIGHT
        self.ball_size = BALL_SIZE

        self.FPS = FPS

        # Players
        self.player1 = pygame.Rect(self.WIDTH - self.player_width * 2,
                                   self.HEIGHT - 50,
                                   self.player_width, self.player_height)

        self.player2 = pygame.Rect(self.player_width, 40,
                                   self.player_width, self.player_height)


        # Ball
        self.ball = pygame.Rect(self.WIDTH - 40, self.HEIGHT - 40,
                                self.ball_size, self.ball_size)
        self.ball_speed_x = 0
        self.ball_speed_y = 0

        # Scores
        self.score_p1 = 0
        self.score_p2 = 0

        # States
        self.waiting_for_serve = True
        self.game_over = False
        self.winner = None

    def start(self):
        try:
            while not self.game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE and self.waiting_for_serve:
                            self.waiting_for_serve = False
                            self.ball_speed_x = INITIAL_BALL_SPEED_X
                            self.ball_speed_y = INITIAL_BALL_SPEED_Y

                keys = pygame.key.get_pressed()
                move_p1 = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
                move_p2 = keys[pygame.K_d] - keys[pygame.K_q]

                self.update(move_p1, move_p2)

                self.screen.fill(BLACK)
                score_text = self.font.render(self.score_label(), True, WHITE)
                self.screen.blit(score_text, (self.WIDTH // 2 - 40, 10))

                if self.waiting_for_serve and not self.game_over:
                    hint = self.font.render("Press SPACE to serve", True, WHITE)
                    self.screen.blit(hint, (self.WIDTH // 2 - 120, self.HEIGHT // 2))

                self.draw()
                self.clock.tick(self.FPS)

            self.display_winner()

            pygame.display.update()
            pygame.time.wait(3000)
        except Exception as e:
            # Basic error handling just in case 
            print(f"Unexpected error {e}")
        finally:
            pygame.quit()
            sys.exit()

    def draw(self):
        pygame.draw.rect(self.screen, WHITE, self.player1)
        pygame.draw.rect(self.screen, WHITE, self.player2)
        pygame.draw.ellipse(self.screen, WHITE, self.ball)
        pygame.display.flip()

    def display_winner(self):
        winner = "Player 1" if self.winner == 1 else "Player 2"
        winner_display = self.font.render(f"{winner} wins", True, WHITE)
        self.screen.blit(winner_display, (self.WIDTH // 2 - 100, self.HEIGHT // 2))

    def move_player(self, player_rect: pygame.Rect, move: int) -> None:
        if move < 0 and player_rect.left > 0:
            player_rect.x -= PLAYER_SPEED
        if move > 0 and player_rect.right < self.WIDTH:
            player_rect.x += PLAYER_SPEED

    def update(self, move_p1: int, move_p2: int) -> None:
        if self.waiting_for_serve:
            self.ball.centerx = self.player1.centerx
            self.ball.bottom = self.player1.top
        else:
            self.move_player(self.player1, move_p1)
            self.move_player(self.player2, move_p2)

            self.ball.x += self.ball_speed_x
            self.ball.y += self.ball_speed_y

        self.check_colissions()

    def score(self, player: int) -> None:
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

    def reset_positions(self) -> None:
        self.ball_speed_x = 0
        self.ball_speed_y = 0
        self.player1.x = self.WIDTH - self.player_width * 2
        self.player2.x = self.player_width

    def check_colissions(self) -> None:
        if self.ball.left <= 0 or self.ball.right >= self.WIDTH:
            self.ball_speed_x = -self.ball_speed_x

        if self.ball.colliderect(self.player1) and self.ball_speed_y > 0:
            self.ball_speed_y = -self.ball_speed_y
        if self.ball.colliderect(self.player2) and self.ball_speed_y < 0:
            self.ball_speed_y = -self.ball_speed_y

        if self.ball.top <= 0 and not self.waiting_for_serve:
            self.score(1)
            self.reset_positions()

        if self.ball.bottom >= self.HEIGHT and not self.waiting_for_serve:
            self.score(2)
            self.reset_positions()

    def score_label(self) -> str:
        if self.game_over:
            return f"Game!"

        if self.score_p1 >= 3 and self.score_p2 >= 3:
            if self.score_p1 == self.score_p2:
                return "Deuce"
            elif self.score_p1 == self.score_p2 + 1:
                return "Advantage Player 1"
            elif self.score_p2 == self.score_p1 + 1:
                return "Advantage Player 2"

        return f"{SCORE_NAMES[self.score_p1]}-{SCORE_NAMES[self.score_p2]}"

if __name__ == "__main__":
    game = TennisGame()
    game.start()
