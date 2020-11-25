# module day7


class Component:
    def __init__(self, name=""):
        self.name = name
        self.input = 0


class PowerSource(Component):
    def __init__(self, power=0):
        self.power = power

    def _get_output(self):
        return self.input

    def _set_power(self, value):
        self.input = value

    def _get_power(self):
        return self.input

    output = property(_get_output)
    power = property(_get_power, _set_power)


class Wire(Component):
    def __init__(self, input_connection=None, name=""):
        self.name = name
        self.input_connection = input_connection

    def connect_input(self, component):
        self.input_connection = component

    def _get_output(self):
        print("getting output of wire:", self.name)
        return int(self.input)

    def _get_input(self):
        if self.input_connection is None:
            return 0
        else:
            return self.input_connection.output

    output = property(_get_output)
    input = property(_get_input)


class Gate(Wire):
    def __init__(self, input_connection=None):
        Wire.__init__(self, input_connection)


class NotGate(Gate):
    def __init__(self, input_connection=None):
        Gate.__init__(self, input_connection)

    def _get_output(self):
        # bitwise compliment
        return ~self.input + 2 ** 16

    output = property(_get_output)


class ShiftGate(Gate):
    def __init__(self, direction, amount, input_connection=None):
        Gate.__init__(self, input_connection)
        self.direction = direction
        self.amount = int(amount)

    def _get_output(self):
        if self.direction == "left":
            return self.input << self.amount
        elif self.direction == "right":
            return self.input >> self.amount
        else:
            raise ValueError("bad direction")

    output = property(_get_output)


class TwoConnectionGate(Gate):
    # Parent class for AND and OR
    def __init__(self, input_connection=None, input_connection2=None):
        Gate.__init__(self, input_connection)
        self.input_connection2 = input_connection2

    def connect_input2(self, component):
        self.input_connection2 = component

    def _get_input2(self):
        if self.input_connection2 is None:
            return 0
        else:
            return self.input_connection2.output

    input2 = property(_get_input2)


class AndGate(TwoConnectionGate):
    def __init__(self, input_connection=None, input_connection2=None):
        TwoConnectionGate.__init__(self, input_connection, input_connection2)

    def _get_output(self):
        return self.input_connection.output & self.input_connection2.output

    output = property(_get_output)


class OrGate(TwoConnectionGate):
    def __init__(self, input_connection=None, input_connection2=None):
        TwoConnectionGate.__init__(self, input_connection, input_connection2)

    def _get_output(self):
        return self.input_connection.output | self.input_connection2.output

    output = property(_get_output)


class BreadBoard:
    def __init__(self, starting_component=None):
        self.components = {}

    def add_component(self, component, key):
        # adds a new component to the components dictionary
        # will replace a component if it exists!
        self.components[key] = component
        self.components[key].name = key

    def add_components(self, *results):
        # takes in a tuple and adds the specified components
        if results[0] == "power":
            self.add_component(PowerSource(results[1]), results[2] + "_power")
            self.add_component(
                self._get_or_create_wire(
                    results[2], self.get_component(results[2] + "_power")
                ),
                results[2],
            )
        elif results[0] == "wire_to_wire":
            self.add_component(
                self._get_or_create_wire(
                    results[2], self._get_or_create_wire(results[1])
                ),
                results[2],
            )
        elif results[0] == "not":
            self.add_component(
                NotGate(self._get_or_create_wire(results[1])), results[1] + "_not"
            )
            self.add_component(
                self._get_or_create_wire(
                    results[2], self.get_component(results[1] + "_not")
                ),
                results[2],
            )
        elif results[0] == "and":
            self.add_component(
                AndGate(
                    self._get_or_create_wire(results[1]),
                    self._get_or_create_wire(results[2]),
                ),
                results[1] + "_and",
            )
            self.add_component(
                self._get_or_create_wire(
                    results[3], self.get_component(results[1] + "_and")
                ),
                results[3],
            )
        elif results[0] == "or":
            self.add_component(
                OrGate(
                    self._get_or_create_wire(results[1]),
                    self._get_or_create_wire(results[2]),
                ),
                results[1] + "_and",
            )
            self.add_component(
                self._get_or_create_wire(
                    results[3], self.get_component(results[1] + "_and")
                ),
                results[3],
            )
        elif results[0] == "shift":
            self.add_component(
                ShiftGate(results[1], results[3], self._get_or_create_wire(results[2])),
                results[2] + "_shift_" + results[1],
            )
            self.add_component(
                self._get_or_create_wire(
                    results[4], self.get_component(results[2] + "_shift_" + results[1])
                ),
                results[4],
            )
        else:
            raise ValueError("bad input")

    def get_component(self, key):
        return self.components[key]

    def _get_or_create_wire(self, key, input_connection=None):
        # utility function to return a wire if it exists, or create and return it if it
        # doesn't
        if key in self.components:
            if self.get_component(key).input_connection is None:
                self.get_component(key).connect_input(input_connection)
            return self.get_component(key)
        else:
            self.add_component(Wire(input_connection, key), key)
            return self.get_component(key)


def parseline(line):
    words = line.split(" ")
    if len(words) == 3:
        if is_number(words[0]):
            return "power", words[0], words[2]
        else:
            return "wire_to_wire", words[0], words[2]
    elif len(words) == 4:
        return "not", words[1], words[3]
    elif len(words) == 5:
        if words[1] == "AND":
            return "and", words[0], words[2], words[4]
        elif words[1] == "OR":
            return "or", words[0], words[2], words[4]
        elif words[1] == "LSHIFT":
            return "shift", "left", words[0], words[2], words[4]
        elif words[1] == "RSHIFT":
            return "shift", "right", words[0], words[2], words[4]
        else:
            raise ValueError("bad operator input")
    else:
        raise ValueError("bad line")


def is_number(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def load_file(inputfilename):
    breadboard = BreadBoard()
    file = open(inputfilename)
    content = file.read()
    for line in content.splitlines():
        results = parseline(line)
        breadboard.add_components(*results)
    print("breadboard loaded")
    return breadboard


def textonly(inputfilename):
    breadboard = load_file(inputfilename)
    return breadboard.get_component("a").output
