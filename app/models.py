def serialize_account(account):
    return {
        "id": str(account["_id"]),
        "name": account["name"],
        "balance": account["balance"]
    }
