import unittest
from advent.days import day9


class GraphTestCase(unittest.TestCase):
    def setUp(self):
        self.cg = day9.CityGraph()
        self.cg.add_edge("Philadelphia", "New York", 96)
        self.cg.add_edge("Philadelphia", "Baltimore", 101)

    def test_1(self):
        self.assertEquals(self.cg.get_distance("Philadelphia", "New York"), 96)

    def test_2(self):
        self.assertEquals(self.cg.get_distance("New York", "Philadelphia"), 96)

    def test_3(self):
        self.assertEquals(self.cg.get_distance("Philadelphia", "Baltimore"), 101)

    def test_4(self):
        self.assertEquals(self.cg.get_distance("Baltimore", "Philadelphia"), 101)

    def test_5(self):
        self.assertEquals(self.cg.get_distance("New York", "Baltimore"), 5)
