import pytest
from stringcalculator.main import add

def test_stringCalculator_should_return_zero_on_empty_string():
    result = add("")
    assert result == 0, "String calculater should return 0 on empty string"

def test_stringCalculator_should_return_same_value_on_single_input():
    result = add("5")
    assert result == 5, "String calculater should return same value on single input"

def test_stringCalculator_return_sumation_on_two_value():
    result = add("5,4")
    assert result == 9, "String calculater should return correct addition for two numbers"

def test_stringCalculator_return_sumation_for_multiple_numbers():
    result = add("5,4,3,2,1")
    assert result == 15, "String calculater should return correct addition for multiple numbers"