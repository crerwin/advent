from advent.day import Day

class Day1(Day):
    year = 2024
    day = 1

    list_a = []
    list_b = []

    def _part1(self):
        self.load_lists_from_input(self.input())
        self.list_a.sort()
        self.list_b.sort()
        return self.get_total_distance_between_lists(self.list_a, self.list_b)
    
    def _part2(self):
        self.load_lists_from_input(self.input())
        return self.get_similarity_score(self.list_a, self.list_b)
    
    def reset_lists(self):
        self.list_a = []
        self.list_b = []
    
    def load_lists_from_input(self, input):
        for line in input.splitlines():
            line_split = line.split()
            self.list_a.append(int(line_split[0]))
            self.list_b.append(int(line_split[1]))
    
    def get_distance(self, a: int, b: int) -> int:
        return abs(a - b)
    
    def get_total_distance_between_lists(self, list_a: list[int], list_b: list[int]) -> int:
        if len(list_a) != len(list_b):
            raise ValueError("lists were not equal in length")
        
        else:
            total_distance = 0
            for i in range(0, len(list_a)):
                total_distance += self.get_distance(list_a[i], list_b[i])
        
        return total_distance
    
    def get_similarity_score(self, list_a: list[int], list_b: list[int]) -> int:
        similarity_score = 0
        for number in list_a:
            similarity_score += number * list_b.count(number)
        
        return similarity_score