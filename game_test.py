from game import TennisGame

###Physical tests to validate scoring when ball crosses top or bottom edges###

def test_player_1_point_after_ball_hits_top():
    game = TennisGame()
    game.score_p1 = 0
    game.waiting_for_serve = False

    #ball crosses the top edge
    game.ball.y = -1
    game.update(move_p1=0, move_p2=0)

    #validate if update method increments player 1 score
    assert game.score_p1 == 1
    assert game.waiting_for_serve == True

def test_player_2_point_after_ball_hits_bottom():
    game = TennisGame()
    game.score_p2 = 0
    game.waiting_for_serve = False

    #ball crosses the bottom edge
    game.ball.y = game.HEIGHT + 1
    game.update(move_p1=0, move_p2=0)

    #validate if update method increments player 2 score
    assert game.score_p2 == 1
    assert game.waiting_for_serve == True

###Scoring tests to validate scoring logic###

def test_score_player_1_increments():
    game = TennisGame()
    game.score_p1 = 0

    game.score(1)

    assert game.score_p1 == 1
    assert game.game_over is False

def test_score_player_2_increments():
    game = TennisGame()
    game.score_p2 = 0

    game.score(2)

    assert game.score_p2 == 1
    assert game.game_over is False


def test_score_player_1_wins_normal_game():
    game = TennisGame()
    game.score_p1 = 4
    game.score_p2 = 2

    game.score(1)

    assert game.score_p1 == 5
    assert game.game_over is True
    assert game.winner == 1


def test_score_deuce_advantage_and_back_to_deuce():
    game = TennisGame()
    game.score_p1 = 4
    game.score_p2 = 4

    # Player 1 advantage
    game.score(1)
    assert (game.score_p1, game.score_p2) == (5, 4)
    assert game.game_over is False

    # Player 2 ties back to deuce
    game.score(2)
    assert (game.score_p1, game.score_p2) == (4, 4)
    assert game.game_over is False


def test_score_player_1_wins_after_advantage():
    game = TennisGame()
    game.score_p1 = 5
    game.score_p2 = 4

    game.score(1)

    assert game.game_over is True
    assert game.winner == 1

###Tests to prevent bugs###

def test_no_point_when_waiting_for_serve_bug():
    game = TennisGame()
    game.score_p1 = 0
    game.score_p2 = 0
    game.waiting_for_serve = True

    #ball crosses the top edge but game is waiting for serve
    game.ball.y = -1
    game.update(move_p1=0, move_p2=0)

    #validate if scores remain unchanged
    assert game.score_p1 == 0
    assert game.score_p2 == 0


