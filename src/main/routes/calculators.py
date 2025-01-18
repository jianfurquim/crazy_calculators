from flask import Blueprint, jsonify, request
from src.calculators.calculator_one import CalculatorOne

calc_route_bp = Blueprint("calc_routes", __name__)


@calc_route_bp.route("/calculator/one", methods=["POST"])
def calculator_one():
    try:
        if not request.is_json:
            return (
                jsonify({"error": "Invalid Content-Type, must be application/json"}),
                400,
            )

        calc = CalculatorOne()
        return jsonify(calc.calculate(request)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
