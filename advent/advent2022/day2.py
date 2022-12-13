from advent.day import Day


class Day2(Day):
    year = 2022
    day = 2

    def _part1(self):
        return score_game(self.input().splitlines(), part=1)

    def _part2(self):
        return score_game(self.input().splitlines(), part=2)


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

move_win_against = {
    "A": "B",
    "B": "C",
    "C": "A",
}

move_lose_against = {
    "A": "C",
    "B": "A",
    "C": "B",
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


def score_game(round_plays, part: int = 1) -> int:
    total_score = 0
    for round_play in round_plays:
        total_score += score_round(round_play, part)

    return total_score


def score_round(round_play: str, part: int = 1) -> int:
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
    if part == 1:
        player_play = move_decrypt[player_play]
    elif part == 2:
        if player_play == "X":
            player_play = move_lose_against[opponent_play]
        elif player_play == "Y":
            player_play = opponent_play
        elif player_play == "Z":
            player_play = move_win_against[opponent_play]
        else:
            raise ValueError(f"Invalid part 2 player play {player_play}")
    else:
        raise ValueError(f"Invalid part specification {part}")
    score += move_score[player_play]
    score += outcome_score(opponent_play, player_play)

    return score
