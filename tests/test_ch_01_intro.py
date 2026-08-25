import pytest
from src.ch_01_intro import ch_01_08_getting_started_with_data as ch_01_08
from src.ch_01_intro import ch_01_09_input_and_output as ch_01_09
from src.ch_01_intro import ch_01_10_control_structures as ch_01_10
from src.ch_01_intro import ch_01_11_exception_handling as ch_01_11
from src.ch_01_intro import ch_01_12_defining_functions as ch_01_12
from src.ch_01_intro import ch_01_13_python_oop as ch_01_13

# CH 01-13 Python OOP Tests
class TestFractions:
    frac1 = ch_01_13.Fraction(3, 4)
    frac2 = ch_01_13.Fraction(6, 8)
    frac3 = ch_01_13.Fraction(2, 3)

    @pytest.mark.parametrize(
        "frac_a, frac_b, expected_result",
        [
            (frac1, frac2, True),
            (frac1, frac3, False),
            (frac2, frac3, False),
        ]
    )
    def test_fraction_deep_equality(self, frac_a: ch_01_13.Fraction, frac_b: ch_01_13.Fraction, expected_result: bool):
        assert (frac_a == frac_b) == expected_result, "Deep equality is not working"

    def test_fraction_addition(self):
        assert self.frac1 + self.frac2 == ch_01_13.Fraction(3, 2), "Addition operator has not been implemented properly"

    def test_fraction_subtraction(self):
        assert self.frac1 - self.frac2 == ch_01_13.Fraction(0, 1), "Subtraction operator has not been implemented properly"


class TestLogicGates:
    def test_abstract_logic_gates(self):
        with pytest.raises(TypeError):
            ch_01_13.LogicGate()
        with pytest.raises(TypeError):
            ch_01_13.BinaryGate()
        with pytest.raises(TypeError):
            ch_01_13.UnaryGate()

    def test_and_gate(self):
        and1 = ch_01_13.AndGate("AND1")

        and1.pin_a = 0
        and1.pin_b = 0
        assert and1.get_output() == 0

        and1.pin_a = 0
        and1.pin_b = 1 
        assert and1.get_output() == 0 

        and1.pin_a = 1
        and1.pin_b = 0 
        assert and1.get_output() == 0 

        and1.pin_a = 1
        and1.pin_b = 1
        assert and1.get_output() == 1

    def test_or_gate(self):
        or1 = ch_01_13.OrGate("OR1")

        or1.pin_a = 0
        or1.pin_b = 0
        assert or1.get_output() == 0, "OR gate is evaluating to True when both imputs are off"

        or1.pin_a = 0
        or1.pin_b = 1 
        assert or1.get_output() == 1 

        or1.pin_a = 1
        or1.pin_b = 0 
        assert or1.get_output() == 1

        or1.pin_a = 1
        or1.pin_b = 1
        assert or1.get_output() == 1