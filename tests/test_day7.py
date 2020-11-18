import unittest
from days import day7


class WireTestCase(unittest.TestCase):
    def test_no_input(self):
        testwire = day7.Wire()
        self.assertEqual(testwire.output, 0)

    def test_input(self):
        test_power_source = day7.PowerSource()
        test_power_source.power = 100
        testwire = day7.Wire()
        self.assertEqual(testwire.output, 0)
        testwire.connect_input(test_power_source)
        self.assertEqual(testwire.output, 100)


class PowerSourceTestCase(unittest.TestCase):
    def test_no_power(self):
        test_power_source = day7.PowerSource()
        test_power_source.power = 0
        self.assertEqual(test_power_source.output, 0)

    def test_some_power(self):
        test_power_source = day7.PowerSource()
        test_power_source.power = 100
        self.assertEqual(test_power_source.output, 100)

    def test_change_power(self):
        test_power_source = day7.PowerSource()
        test_power_source.power = 50
        self.assertEqual(test_power_source.output, 50)
        test_power_source.power = 150
        self.assertEqual(test_power_source.output, 150)

    def test_constructor(self):
        test_power_source = day7.PowerSource(123)
        self.assertEqual(test_power_source.output, 123)


class NotGateTestCase(unittest.TestCase):
    def test_case_1(self):
        test_power_source = day7.PowerSource()
        test_power_source.power = 123
        test_not_gate = day7.NotGate()
        test_not_gate.connect_input(test_power_source)
        self.assertEqual(test_not_gate.output, 65412)


class ShiftGate(unittest.TestCase):
    def test_left_case_1(self):
        test_power_source = day7.PowerSource()
        test_power_source.power = 123
        test_shift_gate = day7.ShiftGate("left", 2)
        test_shift_gate.connect_input(test_power_source)
        self.assertEqual(test_shift_gate.output, 492)

    def test_right_case_1(self):
        test_power_source = day7.PowerSource()
        test_power_source.power = 456
        test_shift_gate = day7.ShiftGate("right", 2)
        test_shift_gate.connect_input(test_power_source)
        self.assertEqual(test_shift_gate.output, 114)


class AndGate(unittest.TestCase):
    def test_and_case_1(self):
        x = day7.PowerSource()
        y = day7.PowerSource()
        x.power = 123
        y.power = 456
        test_and_gate = day7.AndGate()
        test_and_gate.connect_input(x)
        test_and_gate.connect_input2(y)
        self.assertEqual(test_and_gate.output, 72)


class OrGate(unittest.TestCase):
    def test_or_case_1(self):
        x = day7.PowerSource()
        y = day7.PowerSource()
        x.power = 123
        y.power = 456
        test_or_gate = day7.OrGate()
        test_or_gate.connect_input(x)
        test_or_gate.connect_input2(y)
        self.assertEqual(test_or_gate.output, 507)


class WireToWireTest(unittest.TestCase):
    def test_case_1(self):
        x = day7.PowerSource()
        x.power = 123
        y = day7.Wire()
        z = day7.Wire()
        y.connect_input(x)
        z.connect_input(y)
        self.assertEqual(z.output, 123)


class ParseTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(day7.parseline("123 -> x"), ("power", "123", "x"))

    def test_2(self):
        self.assertEqual(day7.parseline("NOT x -> h"), ("not", "x", "h"))

    def test_3(self):
        self.assertEqual(day7.parseline("x AND y -> d"), ("and", "x", "y", "d"))

    def test_4(self):
        self.assertEqual(day7.parseline("x -> y"), ("wire_to_wire", "x", "y"))


class BreadBoardTestCase(unittest.TestCase):
    def test_1(self):
        breadboard = day7.BreadBoard()
        breadboard.add_component(day7.PowerSource(), "testpowersource")
        breadboard.get_component("testpowersource").power = 123
        self.assertEqual(breadboard.get_component("testpowersource").output, 123)
        breadboard.add_component(day7.Wire(), "testwire")
        breadboard.get_component("testwire").connect_input(
            breadboard.get_component("testpowersource")
        )
        self.assertEqual(breadboard.get_component("testwire").output, 123)


class CreateComponentTestCase(unittest.TestCase):
    def setUp(self):
        self.breadboard = day7.BreadBoard()
        self.parseAndAdd("123 -> x")
        self.parseAndAdd("456 -> y")
        self.parseAndAdd("x AND y -> d")
        self.parseAndAdd("x OR y -> e")
        self.parseAndAdd("x LSHIFT 2 -> f")
        self.parseAndAdd("y RSHIFT 2 -> g")
        self.parseAndAdd("NOT x -> h")
        self.parseAndAdd("NOT y -> i")

    def parseAndAdd(self, string_to_parse):
        self.breadboard.add_components(*day7.parseline(string_to_parse))

    def test_1(self):
        self.assertEqual(self.breadboard.get_component("d").output, 72)

    def test_2(self):
        self.assertEqual(self.breadboard.get_component("e").output, 507)

    def test_3(self):
        self.assertEqual(self.breadboard.get_component("f").output, 492)

    def test_4(self):
        self.assertEqual(self.breadboard.get_component("g").output, 114)

    def test_5(self):
        self.assertEqual(self.breadboard.get_component("h").output, 65412)

    def test_6(self):
        self.assertEqual(self.breadboard.get_component("i").output, 65079)

    def test_7(self):
        self.assertEqual(self.breadboard.get_component("x").output, 123)

    def test_8(self):
        self.assertEqual(self.breadboard.get_component("y").output, 456)


class CreateComponentByParsingTestCase(unittest.TestCase):
    def setUp(self):
        self.lines = [
            "123 -> x",
            "456 -> y",
            "123 -> x",
            "456 -> y",
            "x AND y -> d",
            "x OR y -> e",
            "x LSHIFT 2 -> f",
            "y RSHIFT 2 -> g",
            "NOT x -> h",
            "NOT y -> i",
        ]
        self.breadboard = day7.BreadBoard()
        for line in self.lines:
            results = day7.parseline(line)
            self.breadboard.add_components(*results)

    def test_1(self):
        self.assertEqual(self.breadboard.get_component("d").output, 72)

    def test_2(self):
        self.assertEqual(self.breadboard.get_component("e").output, 507)

    def test_3(self):
        self.assertEqual(self.breadboard.get_component("f").output, 492)

    def test_4(self):
        self.assertEqual(self.breadboard.get_component("g").output, 114)

    def test_5(self):
        self.assertEqual(self.breadboard.get_component("h").output, 65412)

    def test_6(self):
        self.assertEqual(self.breadboard.get_component("i").output, 65079)

    def test_7(self):
        self.assertEqual(self.breadboard.get_component("x").output, 123)

    def test_8(self):
        self.assertEqual(self.breadboard.get_component("y").output, 456)


class ParsingWireToWireTestCase(unittest.TestCase):
    def setUp(self):
        self.lines = ["123 -> x", "x -> y"]
        self.breadboard = day7.BreadBoard()
        for line in self.lines:
            results = day7.parseline(line)
            self.breadboard.add_components(*results)

    def test_1(self):
        self.assertEqual(self.breadboard.get_component("y").output, 123)


class ParsingWireToWireTestCase2(unittest.TestCase):
    def setUp(self):
        self.lines = [
            "123 -> a",
            "a -> b",
            "b -> c",
            "c -> d",
            "d -> e",
            "e -> f",
            "f -> g",
        ]
        self.breadboard = day7.BreadBoard()
        for line in self.lines:
            results = day7.parseline(line)
            self.breadboard.add_components(*results)

    def test_1(self):
        self.assertEqual(self.breadboard.get_component("g").output, 123)
