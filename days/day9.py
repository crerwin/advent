#module day9


class CityGraph():
    def __init__(self):
        self.graph = {}
        self.edges = {}

    def add_edge(self, city1, city2, distance):
        self.edges[(city1, city2)] = distance
        self.edges[(city2, city1)] = distance

    def get_distance(self, city1, city2):
        if (city1, city2) in self.edges:
            return self.edges[(city1, city2)]
        else:
            return 5

    # def find_distance(self, city1, city2):
