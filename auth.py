from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["POST"])
def login():
    user_data = request.json  # รับ userId, name, picture
    return jsonify({"status": "ok", "userId": user_data.get("userId")})
