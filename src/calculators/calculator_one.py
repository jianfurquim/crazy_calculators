from typing import Dict
from flask import request as FlaskRequest


class CalculatorOne:
    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        print(input_data)

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise Exception("Body bad formated!")

        input_data = body["number"]
        return input_data
