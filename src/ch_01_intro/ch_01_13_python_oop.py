"""
###########################################################################################
########## Sect 1.13: OOP in Python: Defining Classes
###########################################################################################
* objects have state and methods
* By building a class that implements an abstract data type, a programmer can take advantage of the abstraction 
process and at the same time provide the details necessary to actually use the abstraction in a program. Whenever 
we want to implement an abstract data type, we will do so with a new class.

* Classes can be organized into hierarchies
* A class constructor should always invoke the constructor of its parent before 
continuing on with its own data and behavior

* lambda functions

* map, filter, zip functions
   -> zip produces a "list" of tuples that has length equal to the minimum length of
      the iterables passed in 
* callback functions
* tuple unpacking, *args, **kwargs
* sort by key

"""
import pytest
from abc import ABC, abstractmethod
########## Sect 1.13.1: A Fraction Class

def gcd(n: int, m: int) -> int:
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n


class Fraction:
    def __init__(self, num: int, den: int):
        if den < 0:
            self.num = -1 * num 
            self.den = -1 * den
        else:
            self.num = num
            self.den = den

    def __str__(self):
        return(f"{self.num}/{self.den}")

    def __add__(self, other_frac):
        sum_num = (self.num * other_frac.den) + (other_frac.num * self.den)
        sum_den = self.den * other_frac.den
        if sum_num == 0:
            sum_frac = Fraction(0, 1)
        else:
            divisor = gcd(sum_num, sum_den)
            sum_frac = Fraction(sum_num//divisor, sum_den//divisor)
        return sum_frac

    def __sub__(self, other_frac):
        return self + Fraction(-1 * other_frac.num, other_frac.den)

    def __eq__(self, other_frac):
        if self.num == 0 or other_frac.num == 0:
            fractions_equal = self.num == other_frac.num
        else: 
            divisor_self = gcd(self.num, self.den)
            divisor_other = gcd(other_frac.num, other_frac.den)
            numerators_equal = self.num/divisor_self == other_frac.num/divisor_other
            denominators_equal = self.den/divisor_self == other_frac.den/divisor_other
            fractions_equal = numerators_equal & denominators_equal
        return fractions_equal



########## Sect 1.13.2: Inheritance: Logic Gates and Circuits
class LogicGate(ABC):

    def __init__(self, label: str):
        self.label = label
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

    @abstractmethod
    def perform_gate_logic(self):
        pass
    


class BinaryGate(LogicGate):
    def __init__(self, label: str):
        LogicGate.__init__(self, label)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a is None:
            pin_a = int(input(f"Enter pin A input for {self.label} gate:\n"))
        else:
            pin_a = self.pin_a.get_from_gate().get_output()
        return pin_a

    def get_pin_b(self):
        if self.pin_b is None:
            pin_b = int(input(f"Enter pin B input for {self.label} gate:\n"))
        else:
            pin_b = self.pin_b.get_from_gate().get_output()
        return pin_b

    def set_next_pin(self, source):
        if self.pin_a is None:
            self.pin_a = source
        elif self.pin_b is None:
            self.pin_b = source
        else:
            raise RuntimeError(f"No empty pins for gate {self.label}")


class UnaryGate(LogicGate):

    def __init__(self, label: str):
        LogicGate.__init__(self, label)
        self.pin = None

    def get_pin(self):
        if self.pin is None:
            pin = int(input(f"Enter pin input for {self.label} gate:\n"))
        else:
            pin = self.pin.get_from_gate().get_output()
        return pin

    def set_next_pin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError(f"No empty pins for gate {self.label}")


class AndGate(BinaryGate):

    def __init__(self, label: str):
        super(AndGate, self).__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        if a == 1 and b == 1:
            output = 1
        else:
            output = 0
        return output

class NandGate(BinaryGate):

    def __init__(self, label: str):
        super(NandGate, self).__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        if a == 0 or b == 0:
            output = 1
        else:
            output = 0
        return output


class OrGate(BinaryGate):

    def __init__(self, label: str):
        super(OrGate, self).__init__(label) 

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        if a == 1 or b == 1:
            output = 1
        else:
            output = 0
        return output


class NorGate(BinaryGate):

    def __init__(self, label: str):
        super(NorGate, self).__init__(label) 

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        if a == 0 and b == 0:
            output = 1
        else:
            output = 0
        return output


class NotGate(UnaryGate):

    def __init__(self, label: str):
        super(NotGate, self).__init__(label)

    def perform_gate_logic(self):
        pin = self.get_pin()

        if pin == 0:
            output = 1
        else:
            output = 0
        return output


class Connector:

    def __init__(self, from_gate: LogicGate, to_gate: LogicGate):
        self.from_gate = from_gate
        self.to_gate = to_gate

        to_gate.set_next_pin(self)

    def get_from_gate(self):
        return self.from_gate

    def get_to_gate(self):
        return self.to_gate

if __name__ == "__main__":
    # TEST FRACTION CLASS
    frac1 = Fraction(3, 4)
    frac2 = Fraction(6, 8)
    frac3 = Fraction(2, 3)

    print(f"Fraction 1: {frac1}")
    print(f"Fraction 2: {frac2}")
    print(f"Fraction 3: {frac3}\n")

    print(f"({frac1}) == ({frac2}): {frac1 == frac2}")
    print(f"({frac1}) == ({frac3}): {frac1 == frac3}\n")

    print(f"{frac1} + {frac2} = {frac1 + frac2}")

    print(f"{frac1} - {frac2} = {frac1 - frac2}")

    # TEST LOGICGATE CLASSES
    with pytest.raises(TypeError):
        LogicGate()

    with pytest.raises(TypeError):
        BinaryGate()

    with pytest.raises(TypeError):
        UnaryGate()

#    and_gate = AndGate("AND_GATE_1")
#    print(f"{and_gate.get_output()}\n")
#
#    or_gate = OrGate("OR_GATE_1")
#    print(f"{or_gate.get_output()}\n")
#
#    not_gate = NotGate("NOT_GATE_1")
#    print(f"{not_gate.get_output()}\n")
#
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")

    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)

    print(f"{g4.get_output()}\n")

