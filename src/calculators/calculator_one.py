from typing import Dict
from flask import request as FlaskRequest


class CalculatorOne:
    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        first_proccess_result = self.__first_proccess(input_data)
        second_proccess_result = self.__second_proccess(first_proccess_result)
        third_proccess_result = self.__third_proccess(first_proccess_result)
        calc_result = self.__calculate_result(
            first_proccess_result, second_proccess_result, third_proccess_result
        )
        return self.__format_result(calc_result)

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise Exception("Body bad formated!")

        input_data = body["number"]
        return input_data

    def __first_proccess(self, input_data: float) -> float:
        return input_data / 3

    def __second_proccess(self, input_data: float) -> float:
        first_part = (input_data / 4) + 7
        return (first_part**2) * 0.257

    def __third_proccess(self, input_data: float) -> float:
        first_part = input_data**2.121
        return (first_part / 5) + 1

    def __calculate_result(
        self, first_proccess: float, second_proccess: float, third_proccess: float
    ) -> float:
        return first_proccess + second_proccess + third_proccess

    def __format_result(self, calc_result: float) -> Dict:
        return {"data": {"calculator": 1, "result": round(calc_result, 2)}}
