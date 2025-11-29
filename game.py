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
        pass

    def score(self, player):
        pass

    def check_colissions(self):
        pass

    def update(self, move_p1, move_p2):
        pass 

    def score_label(self):
        #TODO: return the score in tennis format (e.g., "15-30", "Deuce", "Advantage Player 1")
        return f"{self.SCORE_NAMES[self.score_p1]}-{self.SCORE_NAMES[self.score_p2]}"

