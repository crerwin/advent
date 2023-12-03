import logging
import os.path
from jinja2 import Template

logger = logging.getLogger("advent")


def _stubout_year_structure(year: int) -> None:
    year_dir = f"advent/advent{year}"
    year_inputs_dir = f"inputs/{year}"
    init_file = f"{year_dir}/__init__.py"

    logger.info(f"Stubbing out year structure for {year}.")
    if not os.path.exists(year_dir):
        os.mkdir(year_dir)
        logger.info(f"{year_dir} created.")
    else:
        logger.info(f"{year_dir} already exists.")

    if not os.path.exists(year_inputs_dir):
        os.mkdir(year_inputs_dir)
        logger.info(f"{year_inputs_dir} created.")
    else:
        logger.info(f"{year_inputs_dir} already exists.")

    if not os.path.exists(init_file):
        with open("advent/templates/__init__.py.j2", "r") as file:
            init_template = Template(file.read())

        with open(init_file, "w") as output_file:
            output_file.write(init_template.render())
        logger.info(f"{init_file} created.")
    else:
        logger.info(f"{init_file} already exists.")


def _stubout_day_code(year: int, day: int) -> None:
    day_code_file = f"advent/advent{year}/day{day}.py"

    logger.info(f"Generating {day_code_file}")
    logger.debug("opening day.py.j2 template file")
    with open("advent/templates/day.py.j2", "r") as file:
        day_template = Template(file.read())

    day_code = day_template.render(year=year, day=day)

    logger.debug("Templated day code: ")
    logger.debug(day_code)

    if os.path.exists(day_code_file):
        logger.warn(
            f"File {day_code_file} already exists.  Will not overwrite.  Run stubout with --debug if you need the output."
        )
    else:
        logger.info(f"Writing {day_code_file}")
        with open(day_code_file, "w") as output_file:
            output_file.write(day_code)


def _stubout_day_tests(year: int, day: int) -> None:
    day_tests_file = f"tests/test_{year}day{day}.py"

    logger.info(f"Generating {day_tests_file}")
    logger.debug("opening test_day.py.j2 template file")
    with open("advent/templates/test_day.py.j2", "r") as file:
        day_tests_template = Template(file.read())

    day_tests_code = day_tests_template.render(year=year, day=day)

    logger.debug("Templated day tests code:")
    logger.debug(day_tests_code)

    if os.path.exists(day_tests_file):
        logger.warn(
            f"File {day_tests_file} already exists.  Will not overwrite.  Run stubout with --debug if you need the output."
        )
    else:
        logger.info(f"Writing {day_tests_file}")
        with open(day_tests_file, "w") as output_file:
            output_file.write(day_tests_code)


def _create_input_file(year: int, day: int) -> None:
    day_inputs_file = f"inputs/{year}/day{day}input.txt"
    if os.path.exists(day_inputs_file):
        logger.warn(f"File {day_inputs_file} already exists.  Will not overwrite.")
    else:
        logger.info(f"Creating empty input file {day_inputs_file}")
        with open(day_inputs_file, "w"):
            pass


def stubout_day(year: int, day: int) -> None:
    _stubout_year_structure(year)
    _stubout_day_code(year, day)
    _stubout_day_tests(year, day)
    _create_input_file(year, day)

    logger.info(
        f"Templating complete.  You must import the day inside advent/advent{year}/__init__.py"
    )


def stubout_year(year: int) -> None:
    _stubout_year_structure(year)
