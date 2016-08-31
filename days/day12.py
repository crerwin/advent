# module day12


class parser():
    def part_a(self, contents):
        ints = []
        for s in contents.split():
            print(s)
            if s.isdigit():
                ints.append(int(s))
        # ints = int(num) for num in contents.split() if s.isdigit()
        print(ints)
        total = sum(ints)
        return total
