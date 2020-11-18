import click

from .advent2015.day1 import Day1


def _run(year, day, part):
    if year == 2015:
        d = Day1("inputs/day1input.txt")
        print(d.part1())
    else:
        print("not yet implemented")


@click.command()
@click.option("--year", "-y", default=2015, type=int)
@click.option("--day", "-d", default=1, type=int)
@click.option("--part", "-p", default=1, type=int)
def advent(year, day, part):
    _run(year, day, part)
