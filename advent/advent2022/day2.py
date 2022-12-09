from advent.day import Day


class Day2(Day):
    year = 2022
    day = 2

    def _part1(self):
        return score_game(self.input().splitlines())


move_decrypt = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}

move_score = {
    "A": 1,
    "B": 2,
    "C": 3,
}


def outcome_score(opponent_play: str, player_play: str) -> int:
    win = 6
    lose = 0
    draw = 3

    if opponent_play == "A":
        if player_play == "B":
            return win
        elif player_play == "C":
            return lose
        else:
            return draw

    if opponent_play == "B":
        if player_play == "C":
            return win
        elif player_play == "A":
            return lose
        else:
            return draw

    if opponent_play == "C":
        if player_play == "A":
            return win
        elif player_play == "B":
            return lose
        else:
            return draw


def score_game(round_plays) -> int:
    total_score = 0
    for round_play in round_plays:
        total_score += score_round(round_play)

    return total_score


def score_round(round_play: str) -> int:
    # fail fast if bad input
    if len(round_play) != 3:
        raise ValueError(f"Invalid play provided: {round_play}")

    # pick out opponent's play...
    opponent_play = round_play[0]

    # ...and fail if invalid
    if opponent_play not in ["A", "B", "C"]:
        raise ValueError(f"Invalid opponent play {opponent_play}")

    # pick out player's play...
    player_play = round_play[2]

    # ...and fail if invalid
    if player_play not in ["X", "Y", "Z"]:
        raise ValueError(f"Invalid player play {player_play}")

    score = 0
    player_play = move_decrypt[player_play]
    score += move_score[player_play]
    score += outcome_score(opponent_play, player_play)

    return score
