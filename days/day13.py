# module day13


class Person():
    def __init__(self, name):
        self.name = name
        self.opinions = {}

    def add_opinion(self, name, opinion):
        self.opinions[name] = opinion

    def get_opinion(self, name):
        return self.opinions[name]


class People():
    def __init__(self):
        self.people = {}

    def get_or_add_person(self, name):
        if name in self.people:
            return self.get_person(name)
        else:
            return self.add_person(name)

    def get_person(name):
        return self.people[name]

    def add_person(name):
        self.people[name] = Person(name)
        return self.people[name]


class Seat():
    def __init__(self, person):
        self.person = person

    def add_right_neighbor(self, seat):
        self.right_neighbor = seat

    def add_left_neighbor(self, seat):
        self.left_neighbor = seat


class SeatingChart():
    def __init__(self, seat):
        self.starting_seat = seat

    def get_overall_opinion(self):
        




def parser(line):
    words = line.split(" ")
    if len(words) != 11:
        raise ValueError("bad input")
    else:
        subject = words[0]
        opinion_target = words[10][0:-1]
        if words[2] == "gain":
            opinion = int(words[3])
        elif words[2] == "lose":
            opinion = int(words[3]) * -1
        else:
            raise ValueError("bad input: expected gain or lose")
        return subject, opinion_target, opinion
