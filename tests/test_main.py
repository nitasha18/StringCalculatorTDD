import pytest
from stringcalculator.main import add

def test_stringCalculator_should_return_zero_on_empty_string():
    result = add("")
    assert result == 0, "String calculater should return 0 on empty string"