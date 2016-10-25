# module day14


class reindeer():
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



class race():
    def __init__(self, reindeer1, reindeer2):
        self.reindeer1 = reindeer1
        self.reindeer2 = reindeer2

    def run(self, time):
        if self.reindeer1.run(time) > self.reindeer2.run(time):
            return self.reindeer1.name
        else:
            return self.reindeer2.name
