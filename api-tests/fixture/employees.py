import uuid

def valid_employee(username="user", first="Alice", last="Harper", deps=1, salary=50000):
    return {
        "id": str(uuid.uuid4()),
        "username": f"{username}-{uuid.uuid4().hex[:6]}",
        "firstName": first,
        "lastName": last,
        "dependants": deps,
        "salary": salary
    }