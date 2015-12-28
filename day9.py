#module day9


class CityGraph():
    def __init__(self):
        graph = {}

    def add_edge(self, city1, city2, distance):
        self.graph[(city1, city2)] = distance


