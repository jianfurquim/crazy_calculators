from flask import Blueprint, jsonify, request

calc_route_bp = Blueprint("calc_routes", __name__)


@calc_route_bp.route("/calculator/one", methods=["POST"])
def calculator_one():
    return jsonify({"success": True}), 200
