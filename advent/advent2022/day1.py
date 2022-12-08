from advent.day import Day


class Day1(Day):
    year = 2022
    day = 1

    def _part1(self):
        return find_highest_calorie_count(self.input().splitlines())

    def _part2(self):
        return find_top_three_calorie_counts(self.input().splitlines())


def find_highest_calorie_count(inventories):
    highest_calorie_count = 0
    current_calorie_count = 0
    for item in inventories:
        if item == "":
            # we've reached a new elf

            # record a new high if the most recent elf was the highest
            if highest_calorie_count < current_calorie_count:
                highest_calorie_count = current_calorie_count

            # reset for a new elf
            current_calorie_count = 0
        else:
            try:
                current_calorie_count += int(item)
            except ValueError:
                print(f"Can't parse int from {item}")

    return highest_calorie_count


def find_top_three_calorie_counts(inventories):
    highest_calorie_counts = [0, 0, 0]
    current_calorie_count = 0

    for item in inventories:
        if item == "":
            # we've reached a new elf

            # record a new high if the most recent elf was the highest
            highest_calorie_counts.append(current_calorie_count)
            highest_calorie_counts = sorted(highest_calorie_counts, reverse=True)[:-1]

            # reset for a new elf
            current_calorie_count = 0
        else:
            try:
                current_calorie_count += int(item)
            except ValueError:
                print(f"Can't parse int from {item}")

    # I don't love repeating this.  It should be its own function.
    highest_calorie_counts.append(current_calorie_count)
    highest_calorie_counts = sorted(highest_calorie_counts, reverse=True)[:-1]

    return (
        highest_calorie_counts[0]
        + highest_calorie_counts[1]
        + highest_calorie_counts[2]
    )
