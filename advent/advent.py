import click
from advent import (
    advent2015,
    advent2016,
    advent2017,
    advent2018,
    advent2019,
    advent2020,
)


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

    def run_day(self, year, day, part):
        yr = self.days[str(year)]
        if day in yr.keys():
            return self.days[str(year)][day]().part(part)
        else:
            return f"Day {day} not yet implemented for year {year}."

    def show(self):
        for k in self.days:
            print(k)
            for d in self.days[k]:
                print(f"  Day {d}")


def _run(year, day, part):
    advent_calendar = AdventCalendar()
    print(advent_calendar.run_day(year, day, part))


@click.group()
def advent():
    pass


@advent.command()
@click.option("--year", "-y", default=2015, type=int)
@click.option("--day", "-d", default=1, type=int)
@click.option("--part", "-p", default=1, type=int)
def run(year, day, part):
    _run(year, day, part)


@advent.command()
def show():
    advent_calendar = AdventCalendar()
    advent_calendar.show()
