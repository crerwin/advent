import pytest
from .test_day import DayTest
from advent.advent2017 import day5


def test_maze_runner_type_1():
    test_maze_1 = """
0
3
0
1
-3
"""

    test_maze_runner = day5.MazeRunner(test_maze_1, 1)
    assert test_maze_runner.maze == [0, 3, 0, 1, -3]
    assert test_maze_runner.position == 0
    assert test_maze_runner.steps == 0
    test_maze_runner.execute_step()
    assert test_maze_runner.maze == [1, 3, 0, 1, -3]
    assert test_maze_runner.position == 0
    assert test_maze_runner.steps == 1
    test_maze_runner.execute_step()
    assert test_maze_runner.maze == [2, 3, 0, 1, -3]
    assert test_maze_runner.position == 1
    assert test_maze_runner.steps == 2
    test_maze_runner.execute_step()
    assert test_maze_runner.maze == [2, 4, 0, 1, -3]
    assert test_maze_runner.position == 4
    assert test_maze_runner.steps == 3
    test_maze_runner.execute_step()
    assert test_maze_runner.maze == [2, 4, 0, 1, -2]
    assert test_maze_runner.position == 1
    assert test_maze_runner.steps == 4
    test_maze_runner.execute_step()
    assert test_maze_runner.maze == [2, 5, 0, 1, -2]
    assert test_maze_runner.position == 5
    assert test_maze_runner.steps == 5


def test_run_maze():
    test_maze_1 = """
0
3
0
1
-3
"""

    test_maze_runner = day5.MazeRunner(test_maze_1, 1)
    assert test_maze_runner.run_maze() == 5


def test_run_maze_type_2():
    test_maze_1 = """
0
3
0
1
-3
"""

    test_maze_runner = day5.MazeRunner(test_maze_1, 2)
    assert test_maze_runner.run_maze() == 10


@pytest.mark.day
class TestDay5(DayTest):
    test_day = day5.Day5()
    expected_part_1 = "336905"
    expected_part_2 = "21985262"
