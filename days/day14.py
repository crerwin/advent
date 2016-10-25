# module day14


class Reindeer():
    def __init__(self, speed, fly_time, rest_time, name="John Doe"):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time

    def run(self, time):
        seconds = 0
        distance = 0
        while seconds < time:
            if seconds + self.fly_time >= time:
                distance += self.speed * (time - seconds)
                seconds = time
            else:
                seconds += self.fly_time
                distance += self.speed * self.fly_time
                if seconds + self.rest_time >= time:
                    seconds = time
                else:
                    seconds += self.rest_time
        return distance



class Race():
    def __init__(self, reindeers):
        self.reindeers = reindeers

    def run(self, time):
        self.reindeers.sort(key=lambda reindeer: reindeer.run(time), reverse=True)
        return self.reindeers[0].name, self.reindeers[0].run(time)


class OfficialRace():
    # input is small enough that we don't need to read from a file

    def run(self):
        self.time = 2503
        self.reindeers = []
        self.reindeers.append(Reindeer(8, 8, 53, "Vixen"))
        self.reindeers.append(Reindeer(13, 4, 49, "Blitzen"))
        self.reindeers.append(Reindeer(20, 7, 132, "Rudolph"))
        self.reindeers.append(Reindeer(12, 4, 43, "Cupid"))
        self.reindeers.append(Reindeer(9, 5, 38, "Donner"))
        self.reindeers.append(Reindeer(10, 4, 37, "Dasher"))
        self.reindeers.append(Reindeer(3, 37, 76, "Comet"))
        self.reindeers.append(Reindeer(9, 12, 97, "Prancer"))
        self.reindeers.append(Reindeer(37, 1, 36, "Dancer"))

        return Race(self.reindeers).run(self.time)
