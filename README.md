This project is an API automation framework built with Python, Pytest, and Requests.

Features:

- Token-based authentication support
- CRUD test coverage (GET, POST, PUT, DELETE)
- JSON schema validation
- Data-driven testing with external test data
- Pytest HTML reporting
- CI/CD with GitHub Actions

How to Run:

```bash
Set PYTHONPATH (Windows PowerShell)
$env:PYTHONPATH = "."
pytest tests --html=reports/report.html