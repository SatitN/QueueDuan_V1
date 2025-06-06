from flask import Blueprint, request, jsonify
from utils import get_sheet, is_duplicate, append_booking, delete_booking

booking_bp = Blueprint("booking", __name__)

@booking_bp.route("/", methods=["POST"])
def create_booking():
    data = request.json
    user_id = data.get("userId")
    datetime = data.get("datetime")

    if is_duplicate(user_id, datetime):
        return jsonify({"status": "duplicate"}), 409

    append_booking(user_id, datetime, data.get("service"))
    return jsonify({"status": "success"})

@booking_bp.route("/cancel", methods=["POST"])
def cancel_booking():
    data = request.json
    deleted = delete_booking(data.get("userId"), data.get("datetime"))
    return jsonify({"status": "deleted" if deleted else "not_found"})
