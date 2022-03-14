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

def test_stringCalculator_return_sumation_with_newline_delimiter():
    result = add("1\n2,3")
    assert result == 6, "String calculater should return correct addition for inputs separated with newline delimeter"

def test_stringCalculator_return_sumation_with_different_delimiter():
    result = add("//;\n1;2,3-$4\n")
    assert result == 10, "String calculater should return correct addition for inputs separated with different delimeter"

def test_stringCalculator_throws_exception_with_negative_numbers():
    with pytest.raises(ValueError) as e:
        add("//;\n1;2-4,3-$4\n-3")
    assert str(e.value) == "Negatives are not allowed [-4, -3]", "String calculater should throw exception on negative inputs"

def test_stringCalculator_handles_numbers_greater_than_thousand():
    result = add("//;\n1002,2")
    assert result == 2, "String calculater should ignore numbers bigger than 1000"

def  test_stringCalculator_should_allow_multiple_and_longer_delimeters():
    result = add("//[***]\n1***2***3")
    assert result == 6, "String calculater should return 6 for \"//[***]\n1***2***3\" string"

    result = add("//[*][%]\n1*2%3")
    assert result == 6, "String calculater should return 6 for \//[*][%]\n1*2%3\" string"  