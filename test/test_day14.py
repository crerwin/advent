import unittest
from advent.days import day14

class ReindeerTestCase(unittest.TestCase):
    def test_reindeer_1(self):
        self.test_reindeer = day14.Reindeer(10, 20, 50)
        self.assertEqual(10, self.test_reindeer.speed)
        self.assertEqual(20, self.test_reindeer.fly_time)
        self.assertEqual(50, self.test_reindeer.rest_time)


class ReindeerRunTestCase1(unittest.TestCase):
    def test_reindeer_shortrun(self):
        self.test_reindeer = day14.Reindeer(10, 20, 50)
        self.assertEqual(50, self.test_reindeer.run(5))
        self.assertEqual(0, self.test_reindeer.run(0))
        self.assertEqual(100, self.test_reindeer.run(10))
        self.assertEqual(200, self.test_reindeer.run(20))

    def test_reindeer_longrun(self):
        self.test_reindeer = day14.Reindeer(10, 20, 50)
        self.assertEqual(200, self.test_reindeer.run(30))
        self.assertEqual(200, self.test_reindeer.run(69))
        self.assertEqual(210, self.test_reindeer.run(71))

    def test_reindeer_2(self):
        self.test_reindeer = day14.Reindeer(14, 10, 127)
        self.assertEqual(1120, self.test_reindeer.run(1000))

    def test_reindeer_3(self):
        self.test_reindeer = day14.Reindeer(16, 11, 162)
        self.assertEqual(1056, self.test_reindeer.run(1000))


class RaceRunTestCase(unittest.TestCase):
    def test_race_1(self):
        self.reindeer1 = day14.Reindeer(14, 10, 127, "Comet")
        self.reindeer2 = day14.Reindeer(16, 11, 162, "Dancer")
        self.race = day14.Race([self.reindeer1, self.reindeer2])
        self.assertEqual(self.reindeer1.name, self.race.run(1000)[0])
