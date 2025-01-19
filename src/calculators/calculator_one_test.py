from typing import Dict
from pytest import raises
from src.calculators.calculator_one import CalculatorOne


class MockRequest:
    def __init__(self, body: Dict):
        self.json = body


def test_calculator_one_format_response():
    mock_request = MockRequest({"number": 1})

    calculator_one = CalculatorOne()
    response = calculator_one.calculate(mock_request)

    assert "data" in response
    assert "calculator" in response["data"]
    assert "result" in response["data"]


def test_calculator_one_correct_response():
    mock_request = MockRequest({"number": 1})

    calculator_one = CalculatorOne()
    response = calculator_one.calculate(mock_request)
    assert response["data"]["result"] == 14.25


def test_calculator_one_body_bad_formated():
    mock_request = MockRequest({"something_error": 1})

    calculator_one = CalculatorOne()

    with raises(Exception) as exception_info:
        calculator_one.calculate(mock_request)

    assert str(exception_info.value) == "Body bad formated!"
    assert exception_info.type == Exception
