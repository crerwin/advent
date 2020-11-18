import click
from advent import advent2015, advent2016, advent2017, advent2018, advent2019, advent2020


class AdventCalendar(object):
    # Each year is an Advent Calendar for organization purposes
    def __init__(self):
        self.days = {}
        self.days['2015'] = advent2015.days
        self.days['2016'] = advent2016.days
        self.days['2017'] = advent2017.days
        self.days['2018'] = advent2018.days
        self.days['2019'] = advent2019.days
        self.days['2020'] = advent2020.days

    def run_day(self, year, day, part):
        return self.days[str(year)][day-1].part(part)


def _run(year, day, part):
    advent_calendar = AdventCalendar()
    print(advent_calendar.run_day(year, day, part))


@click.command()
@click.option("--year", "-y", default=2015, type=int)
@click.option("--day", "-d", default=1, type=int)
@click.option("--part", "-p", default=1, type=int)
def advent(year, day, part):
    _run(year, day, part)
