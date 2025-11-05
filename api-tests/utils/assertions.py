def assert_status(resp, expected):
    assert resp.status_code == expected, f"Expected {expected}, got {resp.status_code}, body={resp.text}"