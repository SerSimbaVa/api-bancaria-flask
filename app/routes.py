from flask import Blueprint, request, jsonify
from app.services import create_account, list_accounts, update_balance
from app.models import serialize_account

account_bp = Blueprint('account_bp', __name__)


@account_bp.route("/accounts", methods=["POST"])
def create():
    data = request.json
    if "name" not in data:
        return jsonify({"error": "Missin name"}), 400
    account_id = create_account(data)
    return jsonify(account_id), 201


@account_bp.route("/accounts", methods=["GET"])
def list_all():
    accounts = list_accounts()
    return jsonify([serialize_account(acc) for acc in accounts])


@account_bp.route("/accounts/<account_id>", methods=["PATCH"])
def update(account_id):
    data = request.get_json()
    if "amount" not in data:
        return jsonify({"error": "Missing amount"}), 400

    new_balance = update_balance(account_id, data["amount"])
    if new_balance is None:
        return jsonify({"error": "Account not found"}), 404

    return jsonify({"balance": new_balance}), 200
