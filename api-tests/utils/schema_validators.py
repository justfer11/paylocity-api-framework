from jsonschema import validate, ValidationError

EMPLOYEE_SCHEMA = {
    "type": "object",
    "required": ["firstName", "lastName", "username"],
    "properties": {
        "username": {"type": "string", "maxLength": 50},
        "id": {"type": "string", "format": "uuid"},
        "firstName": {"type": "string", "maxLength": 50},
        "lastName": {"type": "string", "maxLength": 50},
        "dependants": {"type": "integer", "minimum": 0, "maximum": 32},
        "salary": {"type": "number"},
        "gross": {"type": "number"},
        "benefitsCost": {"type": "number"},
        "net": {"type": "number"}
    },
    "additionalProperties": True
}

def assert_valid_employee(obj):
    """Validate an employee object against the schema."""
    try:
        validate(instance=obj, schema=EMPLOYEE_SCHEMA)
    except ValidationError as e:
        raise AssertionError(f"Schema validation failed: {e.message}")