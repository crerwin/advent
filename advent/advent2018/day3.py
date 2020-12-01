import logging
from advent.day import Day

logger = logging.getLogger(__name__)


class Day3(Day):
    year = 2018
    day = 3

    def _part1(self):
        fabric = Fabric()
        input = self.input().splitlines()
        for line in input:
            fabric.add_claim(get_claim(line))
        return fabric.get_num_squares_in_overlap()

    def _part2(self):
        return ""


class Fabric(object):
    def __init__(self, size=1000):
        logger.debug(f"initializing fabric of size {size}")
        self.size = size
        self.squares = [[0 for i in range(self.size)] for i in range(self.size)]

    def add_claim(self, claim):
        logger.debug(f"adding claim {claim.x},{claim.y} {claim.width}x{claim.height}")
        max_x = claim.x + claim.width
        max_y = claim.y + claim.height
        if max_x > self.size:
            logger.debug("claim width exceeds fabric boundary.")
            max_x = self.size
        if max_y > self.size:
            logger.debug("claim height exceeds fabric boundary.")
            max_y = self.size
        for i in range(claim.x, max_x):
            for j in range(claim.y, max_y):
                self.squares[i][j] += 1

    def get_num_squares_in_overlap(self):
        count = 0
        logger.debug("scanning fabric for squares claimed by more than one claim.")
        for i in range(self.size):
            for j in range(self.size):
                # logger.debug(f"{self.squares[i][j]} claims at {i},{j}")
                if self.squares[i][j] > 1:
                    count += 1
        return count

    def show(self):
        for i in range(self.size):
            print()
            for j in range(self.size):
                print(self.squares[i][j], end=" ")


class Claim(object):
    def __init__(self, claim_id: int, x: int, y: int, height: int, width: int):
        self.claim_id = claim_id
        self.x = x
        self.y = y
        self.height = height
        self.width = width


def get_claim(input: str) -> Claim:
    parts = input.split()
    if len(parts) != 4:
        print(parts)
        raise ValueError("Bad input")

    id = int(parts[0][1:])

    coords = parts[2].split(",")
    x = int(coords[0])
    y = int(coords[1][:-1])

    dims = parts[3].split("x")
    width = int(dims[0])
    height = int(dims[1])

    return Claim(id, x, y, width, height)
