from advent.day import Day


class Day5(Day):
    year = 2017
    day = 5

    def _part1(self):
        maze_runner = MazeRunner(self.input(), 1)
        return maze_runner.run_maze()

    def _part2(self):
        maze_runner = MazeRunner(self.input(), 2)
        return maze_runner.run_maze()


class MazeRunner(object):
    def __init__(self, maze, maze_type):
        self.maze = self.load_maze(maze)
        self.maze_type = maze_type
        self.position = 0
        self.steps = 0

    def load_maze(self, maze):
        steplist = maze.splitlines()
        steplist_ints = []
        for line in steplist:
            try:
                steplist_ints.append(int(line))
            except ValueError:
                next
        return steplist_ints

    def execute_step(self):
        current_position = self.position
        self.position += self.maze[self.position]
        if self.maze_type == 1:
            self.maze[current_position] += 1
        else:
            if self.maze[current_position] >= 3:
                self.maze[current_position] -= 1
            else:
                self.maze[current_position] += 1
        self.steps += 1

    def run_maze(self):
        while self.position >= 0 and self.position < len(self.maze):
            self.execute_step()
        return self.steps
