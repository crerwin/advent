import click
import logging
from .day import Day
from .template import stubout_day, stubout_year

from advent import (
    advent2015,
    advent2016,
    advent2017,
    advent2018,
    advent2019,
    advent2020,
    advent2021,
    advent2022,
    advent2023,
    advent2024
)

logger = logging.getLogger("advent")


class AdventCalendar(object):
    # Each year is an Advent Calendar for organization purposes
    def __init__(self):
        self.days = {}
        self.days["2015"] = advent2015.days
        self.days["2016"] = advent2016.days
        self.days["2017"] = advent2017.days
        self.days["2018"] = advent2018.days
        self.days["2019"] = advent2019.days
        self.days["2020"] = advent2020.days
        self.days["2021"] = advent2021.days
        self.days["2022"] = advent2022.days
        self.days["2023"] = advent2023.days
        self.days["2024"] = advent2024.days

    def run_day(self, year, day, part):
        yr = self.days[str(year)]
        if day in yr.keys():
            return self.days[str(year)][day]().part(part)
        else:
            return f"Day {day} not yet implemented for year {year}."

    def show(self):
        click.secho("Legend: ", bold=True, nl=False)
        click.secho("Not yet implemented\t", fg="white", nl=False)
        click.secho("Neither part\t", fg="magenta", nl=False)
        click.secho("Part 1 only\t", fg="green", nl=False)
        click.secho("Part 2 only\t", fg="red", nl=False)
        click.secho("Both parts\t", fg="blue", nl=False)
        click.secho("Star total for year", fg="yellow", nl=False)
        # two lines
        click.echo("\n")

        for year in self.days:
            click.secho(f"{year}: ", bold=True, nl=False)
            stars = 0
            for day in range(1, 26):
                if day in self.days[year]:
                    # if a specific day's _part1 does not equal Day._part1 (comparing attributes, not return value), then that day has implemented _part1
                    part1_implemented = self.days[year][day]._part1 != Day._part1
                    part2_implemented = self.days[year][day]._part2 != Day._part2

                    if part1_implemented and part2_implemented:
                        click.secho(f"{day} ", fg="blue", nl=False)
                        stars += 2
                    elif part1_implemented:
                        click.secho(f"{day} ", fg="green", nl=False)
                        stars += 1
                    elif part2_implemented:
                        click.secho(f"{day} ", fg="red", nl=False)
                        stars += 1
                    else:
                        click.secho(f"{day} ", fg="magenta", nl=False)
                else:
                    click.secho(f"{day} ", fg="white", nl=False)
            click.secho(f"\N{white medium star} {stars}", fg="yellow")


def _run(year, day, part):
    advent_calendar = AdventCalendar()
    print(advent_calendar.run_day(year, day, part))


@click.group()
@click.option("--debug", is_flag=True)
def advent(debug):
    if debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug logging on")
    else:
        logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)


@advent.command()
@click.option("--year", "-y", default=2015, type=int)
@click.option("--day", "-d", default=1, type=int)
@click.option("--part", "-p", default=1, type=int)
def run(year, day, part):
    logger.debug(f"Running year: {year} day: {day} part: {part}")
    _run(year, day, part)


@advent.command()
def show():
    advent_calendar = AdventCalendar()
    advent_calendar.show()


@advent.command()
@click.option("--year", "-y", required=True, type=int)
@click.option("--day", "-d", type=int)
def stubout(year: int, day: int):
    if day:
        stubout_day(year, day)
    else:
        stubout_year(year)
