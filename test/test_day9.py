import unittest
import day9


class GraphTestCase(unittest.TestCase):
    def test_1(self):
        cg = day9.CityGraph()
        cg.add_edge("Philadelphia")