import pytest
import uuid
from fixture.employees import valid_employee
from utils.assertions import assert_status


@pytest.mark.parametrize("field,value", [
    pytest.param("username", None, marks=pytest.mark.xfail(reason="API does not enforce required username")),
    pytest.param("firstName", None),
    pytest.param("lastName", None),
])
def test_required_fields_null(api_base_url, auth_header, session, field, value):
    payload = valid_employee()
    payload[field] = value
    resp = session.post(f"{api_base_url}/api/Employees", json=payload, headers=auth_header)
    assert_status(resp, 400)

@pytest.mark.xfail(reason="API returns 200 instead of 404 for nonexistent employee")
def test_get_nonexistent_employee(api_base_url, auth_header, session):
    resp = session.get(f"{api_base_url}/api/Employees/{uuid.uuid4()}", headers=auth_header)
    assert resp.status_code in (404, 400)