from utils.schema_validators import assert_valid_employee
import pytest

@pytest.mark.xfail(reason="API returns 200 with empty body for GET /Employees/{id}")
def test_get_employee_schema(api_base_url, auth_header, session, employee_payload):
    create_resp = session.post(f"{api_base_url}/api/Employees", json=employee_payload, headers=auth_header)
    assert create_resp.status_code == 200

    emp_id = employee_payload["id"]
    resp = session.get(f"{api_base_url}/api/Employees/{emp_id}", headers=auth_header)
    assert resp.status_code == 200

    assert resp.text.strip(), "Expected JSON body but got empty response"
    data = resp.json()
    assert_valid_employee(data)

