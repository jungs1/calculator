# Example Calculator Project

This is a simple Python calculator library with test coverage reporting.

## Project Structure

```
example-python/
├── src/
│   ├── __init__.py
│   └── calculator/
│       ├── __init__.py
│       └── calculator.py
├── tests/
│   ├── __init__.py
│   └── test_calculator.py
├── setup.py
├── requirements-dev.txt
├── pytest.ini
└── .coveragerc
```

## Installation

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install the package in development mode:

```bash
pip install -e .
```

3. Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

## Running Tests

Run the tests with:

```bash
pytest
```

## Generating Coverage Reports

To generate coverage reports:

```bash
# Generate HTML coverage report
pytest --cov=src --cov-report=html

# Generate Cobertura XML report for CI/CD tools
pytest --cov=src --cov-report=xml
```

The Cobertura XML report will be saved as `coverage.xml` in the project root directory.

## Uploading Coverage to the Codecov Service

You can upload the generated coverage report using:

```bash
curl -X POST -H "X-Api-Key: YOUR_API_KEY" --data-binary @coverage.xml http://localhost:8000/api/upload/owner/repository/
```

Replace `YOUR_API_KEY` with your actual API key, and `owner/repository` with your repository identifier. 