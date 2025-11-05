Paylocity API Test Automation Framework
🚀 Automated API testing with Pytest and JSON Schema validation for Paylocity's sample API.

📌 Overview
This framework provides a robust and maintainable structure for testing Paylocity's sample API endpoints.
It leverages Pytest for test execution and JSON Schema for response validation, ensuring reliable and scalable automation for both development and interview/demo scenarios.

🧰 Tech Stack
- Python 3.10+
- Pytest – test runner and assertions
- Requests – HTTP client
- JSON Schema – response structure validation
- GitHub Actions – CI/CD integration

📁 Project Structure
paylocity-api-framework/
├── .github/
│   └── workflows/
│       └── api-tests.yml        # CI workflow for GitHub Actions
├── api-tests/
│   ├── fixture/
│   │   └── employees.py         # Fixtures for employee test data/setup
│   ├── tests/
│   │   ├── test_employees_crud.py     # CRUD operation tests
│   │   ├── test_employees_negative.py # Negative/error scenario tests
│   │   └── test_employees_schema.py   # Schema validation tests
│   ├── utils/
│   │   ├── assertions.py        # Custom assertion helpers
│   │   ├── schema_validators.py # JSON schema validation utilities
│   │   └── conftest.py          # Pytest configuration & shared fixtures
│   └── requirements.txt         # Python dependencies
├── .env                         # Environment variables (local config)
├── .gitignore                   # Git ignore rules
├── README.md                    # Documentation for the framework
├── venv/                        # Virtual environment (local, not tracked)
├── __pycache__/                 # Python cache files (ignored)
└── .pytest_cache/               # Pytest cache (ignored)


✅ Features
- 🔍 Schema-based validation: Ensures API responses match expected structure
- 🧪 Modular test design: Easy to extend and maintain
- 🔄 Reusable fixtures: Centralized setup for consistent test environments
- ⚙️ CI-ready: GitHub Actions workflow included

🚀 Getting Started
1. Clone the repo
git clone https://github.com/justfer11/paylocity-api-framework.git
cd paylocity-api-framework

2. Set up environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Run tests
pytest api-tests/

4. Generate HTML report
pytest --html=report.html

🧪 Sample Test
def test_get_employees_status_code(api_client):
    response = api_client.get("/employees")
    assert response.status_code == 200

📦 CI/CD
This project includes a GitHub Actions workflow (.github/workflows/api-tests.yml) that runs tests automatically on push and pull requests.
