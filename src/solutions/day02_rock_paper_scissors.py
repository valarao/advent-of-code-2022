def calculate_rock_paper_scissors_score_with_recommended_moves(games):
    SHAPE_SCORE_MAP = {
        "X": 1, # Rock
        "Y": 2, # Paper
        "Z": 3  # Scissors
    }

    WIN_SCORE_MAP = {
        ("A", "X"): 3, # Rock vs. Rock -> Draw
        ("A", "Y"): 6, # Rock vs. Paper -> Win
        ("A", "Z"): 0, # Rock vs. Scissors -> Loss
        ("B", "X"): 0, # Paper vs. Rock -> Loss
        ("B", "Y"): 3, # Paper vs. Paper -> Draw
        ("B", "Z"): 6, # Paper vs. Scissors -> Win
        ("C", "X"): 6, # Scissors vs. Rock -> Win
        ("C", "Y"): 0, # Scissors vs. Paper -> Loss
        ("C", "Z"): 3, # Scissors vs. Scissors -> Draw
    }

    def evaluate_game(game):
        opponent_choice, my_choice = game.split(" ")
        shape_score = SHAPE_SCORE_MAP[my_choice]
        win_score = WIN_SCORE_MAP[(opponent_choice, my_choice)]
        return shape_score + win_score

    total_score = 0
    for game in games:
        total_score += evaluate_game(game)

    return total_score

def calculate_rock_paper_scissors_score_with_outcomes(games):
    WIN_SCORE_MAP = {
        "X": 0, # Lose
        "Y": 3, # Draw
        "Z": 6  # Win
    }

    SHAPE_WIN_MAP = {
        ("A", "X"): 3, # Lose against Rock -> Scissors
        ("A", "Y"): 1, # Draw against Rock -> Rock
        ("A", "Z"): 2, # Win against Rock -> Paper
        ("B", "X"): 1, # Lose against Paper -> Rock
        ("B", "Y"): 2, # Draw against Paper -> Paper
        ("B", "Z"): 3, # Win against Paper -> Scissors
        ("C", "X"): 2, # Lose against Scissors -> Paper
        ("C", "Y"): 3, # Draw against Scissors -> Scissors
        ("C", "Z"): 1, # Win against Scissors -> Rock
    }

    def evaluate_game(game):
        opponent_choice, game_outcome = game.split(" ")
        shape_score = SHAPE_WIN_MAP[(opponent_choice, game_outcome)]
        win_score = WIN_SCORE_MAP[(game_outcome)]
        return shape_score + win_score

    total_score = 0
    for game in games:
        total_score += evaluate_game(game)

    return total_score
    