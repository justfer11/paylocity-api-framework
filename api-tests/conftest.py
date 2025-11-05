import os
import base64
import uuid
import pytest
import requests
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def api_base_url():
    return os.getenv("API_BASE_URL", "https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod")

@pytest.fixture(scope="session")
def auth_header():
     token = os.getenv("API_BASIC_AUTH", "Basic VGVzdFVzZXI4MjU6VSZmVFZ4RSRhP2ww")
     return {"Authorization": token, "Content-Type": "application/json"}

@pytest.fixture
def employee_payload():
     return {
        "username": f"user-{uuid.uuid4().hex[:8]}",
        "id": str(uuid.uuid4()),
        "firstName": "Alice",
        "lastName": "Harper",
        "dependants": 2,
        "salary": 52000.0
    }

def _url(base, path):
     return f"{base}{path}"

@pytest.fixture
def session():
     s = requests.Session()
     yield s
     s.close()


    