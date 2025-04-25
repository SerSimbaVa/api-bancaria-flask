from bson.objectid import ObjectId
from app.db import accounts_collection


def create_account(data):
    account = {
        "name": data["name"],
        "balance": data.get("balance", 0.0)
    }
    result = accounts_collection.insert_one(account)
    return str(result.inserted_id)


def list_accounts():
    accounts = accounts_collection.find()
    return [account for account in accounts]


def update_balance(account_id, amount):
    account = accounts_collection.find_one({"_id": ObjectId(account_id)})
    if not account:
        return None
    new_balance = account["balance"] + amount
    accounts_collection.update_one({"_id": ObjectId(account_id)}, {
                                   "$set": {"balance": new_balance}})
    return new_balance
