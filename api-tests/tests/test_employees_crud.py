import uuid
import pytest

def test_create_employee(api_base_url, auth_header, session, employee_payload):
    resp = session.post(f"{api_base_url}/api/Employees", json=employee_payload, headers=auth_header)
    assert resp.status_code == 200, f"Create failed: {resp.status_code}, {resp.text}"

def test_get_all_employees(api_base_url, auth_header, session):
    resp = session.get(f"{api_base_url}/api/Employees", headers=auth_header)
    assert resp.status_code == 200, f"Get all failed: {resp.status_code}, {resp.text}"
    
def test_get_employee_by_id(api_base_url, auth_header, session, employee_payload):
    # Create first
    create_resp = session.post(f"{api_base_url}/api/Employees", json=employee_payload, headers=auth_header)
    assert create_resp.status_code == 200, f"Create failed: {create_resp.status_code}, {create_resp.text}"

    # GET by id
    emp_id = employee_payload["id"]
    resp = session.get(f"{api_base_url}/api/Employees/{emp_id}", headers=auth_header)
    assert resp.status_code == 200, f"Get by id failed: {resp.status_code}, {resp.text}"

def test_update_employee(api_base_url, auth_header, session, employee_payload):
    # Create first
    create_resp = session.post(f"{api_base_url}/api/Employees", json=employee_payload, headers=auth_header)
    assert create_resp.status_code == 200, f"Create failed: {create_resp.status_code}, {create_resp.text}"

    # Update fields (dependants, salary, names)
    updated = dict(employee_payload)
    updated["firstName"] = "Peter"
    updated["dependants"] = 3
    updated["salary"] = 78000.0

    resp = session.put(f"{api_base_url}/api/Employees", json=updated, headers=auth_header)
    assert resp.status_code == 200, f"Update failed: {resp.status_code}, {resp.text}"

    # re-fetch by id
    emp_id = updated["id"]
    get_resp = session.get(f"{api_base_url}/api/Employees/{emp_id}", headers=auth_header)
    assert get_resp.status_code == 200, f"Get after update failed: {get_resp.status_code}, {get_resp.text}"

def test_delete_employee(api_base_url, auth_header, session, employee_payload):
    # Create first
    create_resp = session.post(f"{api_base_url}/api/Employees", json=employee_payload, headers=auth_header)
    assert create_resp.status_code == 200, f"Create failed: {create_resp.status_code}, {create_resp.text}"

    # Delete by id
    emp_id = employee_payload["id"]
    del_resp = session.delete(f"{api_base_url}/api/Employees/{emp_id}", headers=auth_header)
    assert del_resp.status_code == 200, f"Delete failed: {del_resp.status_code}, {del_resp.text}"